#===============================================================================
# Good old utilities code blob.
# 
# Nick Wrobel
# Created: 7/28/15
# Modified: 12/15/15
#===============================================================================

import binascii
import os
import datetime
import time
import uuid
import sys
from binascii import unhexlify, hexlify
from uuid import UUID
import traceback
from collections import namedtuple


def UUIDToBinary(uuid):
    binary = binascii.unhexlify(uuid)       
    return binary
 
def BinaryToUUID(binary):
    uuid = binascii.hexlify(binary).decode()    
    return uuid

def CreateTimestampForDB():
    return int(time.time())

def StringIsEmpty(str):
    if (not str or str.isspace()):
        return True
    # else 
    return False

def StringExceedsMaxLength(str, maxLength):
    if StringIsEmpty(str):
        return False   
    else:
        count = 0
        for char in str:
            count = count + 1
            
        return (count > maxLength)
    
def StringIsUUID(str):
    try:
        val = UUID(str, version=4)
    except Exception:
        # If it's a value error, then the string 
        # is not a valid hex code for a UUID.
        return False
    
    # else
    return True

#-------------------------------------------------------------------------------
# Checks if the data is a number that can be interpreted as a postive int
#-------------------------------------------------------------------------------
def IsPositiveInt(num):
    try:
        if (int(num) < 0):
            return False
        else:
            return True
        
    except Exception:
        return False
        

def ArePositiveInts(numbers):
    try:
        numbers = list(numbers)
        for num in numbers:
            if (not IsPositiveInt(num)):
                return False
    except Exception:
        return False
    # else
    return True

# Returns info about an exception
def GetExceptionInfo(e):
    import JokrBackend.Constants as Const
    
    filename = os.path.split(e.__traceback__.tb_frame.f_code.co_filename)[1]
    lineNum = e.__traceback__.tb_lineno
    exceptionMesssage = str(e.__class__.__name__) + ': ' + str(e) 
    stackTrace = traceback.format_exc()
     
    values = {Const.DataCollection.ParamNames.FILENAME: filename, 
              Const.DataCollection.ParamNames.LINE_NUM: lineNum, 
              Const.DataCollection.ParamNames.EXCEPTION_MESSAGE: exceptionMesssage,
              Const.DataCollection.ParamNames.STACK_TRACE: stackTrace }
    
    return values

#-------------------------------------------------------------------------------
# Returns the results of a query in a named tuple format
#-------------------------------------------------------------------------------
def FetchallAsNamedTuple(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]
    
#-------------------------------------------------------------------------------
# Clears the console window
#-------------------------------------------------------------------------------
def ClearConsole():
    clear = lambda: os.system('clear')
    clear()
    
#-------------------------------------------------------------------------------
# Formats a unix timestamp in a pretty format
#-------------------------------------------------------------------------------
def GetPrettyFormatTimestamp(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

#-------------------------------------------------------------------------------
# Functions to print start and end lines
#-------------------------------------------------------------------------------
def PrintStartLine():
    print()
    print('********************************************************************************')
    
def PrintEndLine():
    print('********************************************************************************')
    print()  
    
def PrintSoftStartLine():
    print()
    print('--------------------------------------------------------------------------------')   
    
def PrintSoftEndLine():
    print('--------------------------------------------------------------------------------')   
    print()
    
#-------------------------------------------------------------------------------
# Function to turn a list into a csv string
#-------------------------------------------------------------------------------
def ListToCSV(list):
    return ",".join(list)

#-------------------------------------------------------------------------------
# CreateSequentialUUIDForDB
# Modified code that creates sequential UUIDs based off of timestamp
# http://www.codeproject.com/Tips/815988/Sequential-GUIDS-in-Python
#-------------------------------------------------------------------------------

def CreateSequentialUUIDForDB():
    # What type of machine are we runing on?
    endian = sys.byteorder # will be 'little' or 'big'
    # Need some random info
    rand_bytes = bytearray()
    rand_bytes += os.urandom(10) #Get 10 random bytes
    
    # Get the current timestamp in miliseconds - makes this sequential
    ts = int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds() * 1000)
    tsbytes = bytearray()
    
    # NOTE: we don't pass endian into long_to_bytes
    tsbytes += long_to_bytes(ts) # Convert long to byte array
    while (len(tsbytes) < 8):  # Make sure to padd some 0s on the front so it is 64 bits
        tsbytes.insert(0, 0) # Python will most likely make it a byte array
    
    guid_bytes = bytearray(16) # 16 bytes is 128 bit
    
    # Combine the random and timestamp bytes into a GUID
    guid_bytes[0] = tsbytes[2]  # Copy timestamp into guid
    guid_bytes[1] = tsbytes[3]
    guid_bytes[2] = tsbytes[4]
    guid_bytes[3] = tsbytes[5]
    guid_bytes[4] = tsbytes[6]
    guid_bytes[5] = tsbytes[7]
    
    guid_bytes[6] = rand_bytes[0]  # Copy rand bytes into guid
    guid_bytes[7] = rand_bytes[1]
    guid_bytes[8] = rand_bytes[2]
    guid_bytes[9] = rand_bytes[3]
    guid_bytes[10] = rand_bytes[4]
    guid_bytes[11] = rand_bytes[5]
    guid_bytes[12] = rand_bytes[6]
    guid_bytes[13] = rand_bytes[7]
    guid_bytes[14] = rand_bytes[8]
    guid_bytes[15] = rand_bytes[9]
 
    # Return the uuid as binary
    return bytes(guid_bytes)
    
# Helper function for CreateSequentialUUID
def long_to_bytes (val, endianness='big'):
    """ Pulled from http://stackoverflow.com/questions/8730927/convert-python-long-int-to-fixed-size-byte-array
    Use :ref:`string formatting` and :func:`~binascii.unhexlify` to
    convert ``val``, a :func:`long`, to a byte :func:`str`.

    :param long val: The value to pack

    :param str endianness: The endianness of the result. ``'big'`` for
      big-endian, ``'little'`` for little-endian.

    If you want byte- and word-ordering to differ, you're on your own.

    Using :ref:`string formatting` lets us use Python's C innards.
    """

    # one (1) hex digit per four (4) bits
    width = val.bit_length()

    # unhexlify wants an even multiple of eight (8) bits, but we don't
    # want more digits than we need (hence the ternary-ish 'or')
    width += 8 - ((width % 8) or 8)

    # format width specifier: four (4) bits per hex digit
    fmt = '%%0%dx' % (width // 4)

    # prepend zero (0) to the width, to zero-pad the output
    s = unhexlify(fmt % val)

    if endianness == 'little':
        # see http://stackoverflow.com/a/931095/309233
        s = s[::-1]

    return s


        
                

    
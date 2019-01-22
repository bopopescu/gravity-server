#-------------------------------------------------------------------------------
# GCMManger
# Module to perform routines related to GCM
# 
# Nick Wrobel
# Created: 3/9/16
# Modified: 3/9/16
#-------------------------------------------------------------------------------
import requests
import collections
import simplejson as json
import JokrBackend.Constants as Const 

#-------------------------------------------------------------------------------
# Subscribes a user to a thread, given the user's instanceID
#-------------------------------------------------------------------------------
def SubscribeUserToThread(instanceID, threadID):
    
    topicName = Const.GCM.THREAD_TOPIC_PREFIX + threadID

    url = 'https://iid.googleapis.com/iid/v1/%s/rel/topics/%s' \
        % (instanceID, topicName)
    
    headers = {'Content-Type': 'application/json',
               'Authorization':'key=%s' % Const.GCM.API_KEY }
    
    
    response = requests.post(url, headers=headers)
    
    # If the request was successful, we can assume 1 more user has subscribed.
    # Send out a message 
    # TODO
    
    # return the response code from google
    return response.status_code

#-------------------------------------------------------------------------------
# BroadcastReplyToSubscribers
# Sends out a recent reply to all subscribers of the reply's parent thread.
#-------------------------------------------------------------------------------
def BroadcastReplyToSubscribers(parentThreadID, newReplyJSON):
    
    topicName = Const.GCM.THREAD_TOPIC_PREFIX + parentThreadID
    url = 'https://gcm-http.googleapis.com/gcm/send'

    headers = {'Content-Type': 'application/json',
               'Authorization':'key=%s' % Const.GCM.API_KEY }


    payload = {'to': '/topics/%s' % topicName,
               'data': newReplyJSON
               }
    
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    
    # return the response code from google
    return response.status_code
    
    
    
    

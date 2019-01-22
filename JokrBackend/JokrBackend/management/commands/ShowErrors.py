#------------------------------------------------------------------------------ 
# Command to fetch and display the most recent server exceptions from python 
# code from the database.
#
# Nick Wrobel
# Created: 1/4/16
# Modified: 3/4/16 
#------------------------------------------------------------------------------ 
from JokrBackend.models import Error
from django.core.management import BaseCommand
import JokrBackend.Custom.Utils as Utils
from JokrBackend.DataCollection import DataCollector

# Create a class Command to use django manage command functionality
class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument('--num', required=False, default=3) 
         
    # A command must define handle(), all work happens here
    def handle(self, *args, **options): 
        numberToDisplay = int(options['num'])
        
        # Get the most recent errors
        recentErrors = Error.objects.order_by('-timeCreated')[:numberToDisplay]   
    
        Utils.ClearConsole()
        errors = DataCollector.ServerErrorsToString(recentErrors)
                
        # Print each one, in reversed list order
        # (Console printing stops at the last thing printed)
        for error in reversed(errors):
            print(error)
                            
        
                

        
        
        
            
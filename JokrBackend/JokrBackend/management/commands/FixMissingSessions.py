from django.core.management import BaseCommand
import JokrBackend.Constants as Const
from JokrBackend.models import Session, OnlineContent

class Command(BaseCommand): 
#-------------------------------------------------------------------------------
# handle
# the 'main method'
#-------------------------------------------------------------------------------
    def handle(self, *args, **options): 
        
        dummySession = Session.objects.get(id=Const.Database.Defaults.ID)
        content = OnlineContent.objects.all()
        
        for c in content:
            try:
                c.fromSession.id         
            except Exception:
                c.fromSession = dummySession
                c.save()
                print('ERROR, REWRITING SESSION DATA')
            
        
        
        
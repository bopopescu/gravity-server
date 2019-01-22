#===============================================================================
# URL 'routing table'
# Maps URL requests to Views
#
# Nick Wrobel
# Created: 4/21/15
# Modified: 1/3/16
#===============================================================================
from django.conf.urls import url
# from JokrBackend.Views.Local.UploadLocalPostView import UploadLocalPost
# from JokrBackend.Views.Local.GetLocalPostView import GetLocalPost
# from JokrBackend.Views.Message.UploadMessageView import UploadMessage
# from JokrBackend.Views.Message.GetMessageView import GetMessage
from JokrBackend.Views.Live.UploadLiveView import UploadLive
from JokrBackend.Views.Live.GetLiveView import GetLive
from JokrBackend.Views.Live.SubscribeLiveView import SubscribeLive
from JokrBackend.Views.Reply.UploadReplyView import UploadReply
from JokrBackend.Views.Reply.GetReplyView import GetReply
# from JokrBackend.Views.Moderation.BlockView import Block
from JokrBackend.Views.Moderation.ReportView import Report
from JokrBackend.Views.Security.CreateUserView import CreateUser 
from JokrBackend.Views.Security.GetBanInfoView import GetBanInfo
from JokrBackend.Views.Security.LoginView import Login
from JokrBackend.Views.Analytics.AnalyticsFeedbackView import AnalyticsFeedback
from JokrBackend.Views.Handler404View import Handler404

urlpatterns = [
                 
    # Local
    # url(r'^local/upload/', UploadLocalPost),
    # url(r'^local/get/', GetLocalPost),
    
    # Message
    # url(r'^message/upload/', UploadMessage),
    # url(r'^message/get/', GetMessage),
    
    # Live thread
    url(r'^live/upload/', UploadLive),
    url(r'^live/get/', GetLive),
    url(r'^live/subscribe/', SubscribeLive),

    # Live reply
    url(r'^reply/upload/', UploadReply),
    url(r'^reply/get/', GetReply),

    # Moderation
    # url(r'^moderation/block/', Block),
    url(r'^moderation/report/', Report),
  
    # Security
    url(r'^security/create/', CreateUser),
    # url(r'^security/baninfo/', GetBanInfo),
    url(r'^security/login/', Login),  
    
    # Analytics
    url(r'^analytics/feedback/', AnalyticsFeedback),
   
]

# Set the default view for a 404 error
handler404 = Handler404

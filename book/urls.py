from . import views
from django.urls import path
from logsignup.settings import DEBUG,STATIC_URL,STATIC_ROOT,MEDIA_URL,MEDIA_ROOT

from django.conf.urls.static import static


urlpatterns = [
	path('library',views.library,name='library'),
    path('upload',views.upload,name='upload')
]

if DEBUG:
    urlpatterns += static(STATIC_URL,document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL,document_root=MEDIA_ROOT)
    
	

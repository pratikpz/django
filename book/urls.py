from . import views
from logsignup.settings import DEBUG,STATIC_URL,STATIC_ROOT,MEDIA_ROOT,MEDIA_ROOT

from django.conf.urls.static import static

urlpatterns = [
	path('library',views.library,name='library'),
]

if DEBUG:
    urlpatterns += static(STATIC_URL,document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL,document_root=MEDIA_ROOT)
    
	

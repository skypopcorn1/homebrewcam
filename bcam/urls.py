from django.conf.urls import include, url
from . import views

app_name = 'bcam'

urlpatterns = [
    url(r'^$', views.site_home, name="home"),
	url(r'^upload/(?P<filename>[^/]+)$', views.FileUploadView.as_view(), name='upload')
    ]

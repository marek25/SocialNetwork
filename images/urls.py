from django.conf.urls import url
from django.urls import reverse
from . import views
#from django.urls import path

app_name = 'images'

urlpatterns = [
		url(r'^create/$', views.image_create, name = 'create'),
		url(r'^detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.image_detail, name='detail'),
    	#url(r'^detail/<int:id>/<slug:slug>/$', views.image_detail, name='detail'),
    	url(r'^like/$', views.image_like, name='like'),
    	url(r'^$', views.image_list, name='list'),
    	url(r'^ranking/$', views.image_ranking, name='create'),
    	#url('ranking/', views.image_ranking, name='create'),
]
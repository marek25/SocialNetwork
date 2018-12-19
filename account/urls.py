from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views




urlpatterns = [

	#url(r'^login/$', views.user_login, name = 'login'),
	url(r'^$', views.dashboard, name='dashboard'),

	url(r'^register/$', views.register, name='register'),
	url(r'^edit/$', views.edit, name = 'edit'), 

	#login and logout urls
	url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
	url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
	#url(r'^logout-then-login/$', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),


	# change password urls -STARI KODOVI:
	url(r'^password-change/$', auth_views.PasswordChangeView.as_view(), name="password_change"),
	url(r'^password-change/done/$', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),


	    # change password urlsd_change'),
 #	PREKONTROLISI OVE SVE URL-OVE
  
 	url(r'^password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset/<uidb64>/<token>/$', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
  


   #USER PROFILES
	url(r'^users/$', views.user_list, name='user_list'),  
	url(r'^users/follow/$', views.user_follow, name = 'user_follow'),   
	url(r'^users/(?P<username>[-\w]+)/$', views.user_detail, name='user_detail'),
    # alternative way to include authentication views
    # path('', include('django.contrib.auth.urls')),
  #  path('register/', views.register, name='register'),
   # path('edit/', views.edit, name='edit'),
]



	
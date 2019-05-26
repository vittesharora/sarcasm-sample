from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
# from accounts.views import register, leaderboard, home, rules


urlpatterns=[
	path('',views.opening, name='opening'),
	path('game',views.gaming, name='gaming'),
	path('question/<int:pk>',views.detail,name='detail'),
	path('login',auth_views.login, name='login'), 
	path('register', views.register, name='register'),
	#add a folder registration and then add a login =. html and in settings.py write LOGIN_REDIRECT_URL = '/'
	# path('register',views.register, name='register'),
]

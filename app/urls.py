from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path("signup",views.signup,name="signup"),
    path('log_in',views.log_in,name = 'login'),
    path('profile',views.profile,name='profile'),
    path('logout',views.logout,name= 'logout')
]
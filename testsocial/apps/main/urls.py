from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login_view, name="login"),
    path("reg", views.registration_view, name="reg"),
    path('chat', views.chat_view, name='chat'),
    path('logout', LogoutView.as_view(next_page=views.index), name='logout'),
    path('', views.index, name= 'home')

]

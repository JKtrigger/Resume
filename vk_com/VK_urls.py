from django.urls import path

from vk_com import views

urlpatterns = [
    path('', views.VkComView.as_view(), name='friends'),
    path('login', views.LoginVK.as_view(), name='login_logon'),
]

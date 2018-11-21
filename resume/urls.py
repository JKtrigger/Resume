"""resume URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.generic.base import RedirectView
from django.views.static import serve

from title_page import title_urls, title_views

from vk_com import VK_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vk_api_friends/', include(VK_urls)),
    path(r'', RedirectView.as_view(pattern_name='me-view', permanent=False)),
    path('main/',   include(title_urls)),
    url(r'^static/(?P<path>.*)$', serve, {
        'document_root': settings.STATIC_ROOT, }),
]
handler404 = title_views.handler404

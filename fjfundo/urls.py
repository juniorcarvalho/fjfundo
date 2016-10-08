"""fjfundo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from fjfundo.core.views import dashboard, inicio, account_edit, account_list
from django.contrib.auth.views import logout
from rest_framework.authtoken.views import obtain_auth_token
from fjfundo.api.urls import router

urlpatterns = [
    url(r'^$', inicio, name='inicio'),
    url(r'^dashboard/', dashboard, name='dashboard'),
    url(r'^sair/', logout,
        {'next_page': 'inicio'}, name='logout'),
    url(r'^account_edit/', account_edit, name='account_edit'),
    url(r'^account_list/', account_list, name='account_list'),
    url(r'^api/token/', obtain_auth_token, name='api-token'),
    url(r'^api/', include(router.urls)),
]



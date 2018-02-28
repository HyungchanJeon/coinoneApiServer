"""coinoneApiProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from apiApp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^coinlist/', views.coinlist, name="coinlist"),
    url(r'^balance/', views.balance, name="balance"),
    url(r'^userinfo/', views.userinfo, name="userinfo"),
    url(r'^deposit/', views.deposit, name="deposit"),
    url(r'^limitsell/(?P<currency>[-\w]+)/(?P<price>[-\w]+)/(?P<qty>\d+\.\d+)/$', views.limitsell, name="limitsell"),
    url(r'^limitsell/(?P<currency>[-\w]+)/(?P<price>[-\w]+)/(?P<qty>\d+)/$', views.limitsell, name="limitsell"),
    url(r'^limitbuy/(?P<currency>[-\w]+)/(?P<price>[-\w]+)/(?P<qty>\d+\.\d+)/$', views.limitbuy, name="limitbuy"),
    url(r'^limitbuy/(?P<currency>[-\w]+)/(?P<price>[-\w]+)/(?P<qty>\d+)/$', views.limitbuy, name="limitbuy"),
]

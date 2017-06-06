"""hotelbooking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from booking import views

#app_name = 'booking'

urlpatterns = [
    url(r'^availability/$', views.availability,name ='avail'),
    url(r'^contact/$', views.contact,name ='contact'),
    url(r'^hotel/$', views.hotel,name ='hotel'),
    url(r'^index/$', views.index,name ='index'),
    url(r'^index_jp/$', views.index_jp,name ='index_jp'),
    url(r'^index_fr/$', views.index_fr,name ='index_fr'),
    url(r'^index_cn/$', views.index_cn,name ='index_cn'),
    url(r'^index_ar/$', views.index_ar,name ='index_ar'),
    url(r'^price/$', views.price,name ='price'),
    #url(r'^projects/$', views.projects,name ='projects'),
    url(r'^services/$', views.services,name ='services'),
    #url(r'^sidebar_right/$', views.sidebar_right,name ='sidebar_right'),
    url(r'^table/$', views.table,name ='table'),
    url(r'^search/$', views.search,name ='search'),
    url(r'^payment/$', views.payment,name ='payment'),
]

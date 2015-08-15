"""pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^$','maim.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cereal_list/$','maim.views.cereal_list'),
    # url(r'^get_view/$', 'maim.views.get_view'),
    #url(r'^get_cereal_manu/$', 'maim.views.get_cereal_manu'),
    url(r'^get_cereal_search/$','maim.views.get_cereal_search'),
    url(r'^cereal_search/(?P<cereal>\w+)/$','maim.views.cereal_search'),
    url(r'^get_manufacturer_search/$', 'maim.views.get_manufacturer_search'),
    url(r'^manu_list/$','maim.views.manu_list'),
    url(r'^manu_search/(?P<manufacturer>\w+)/$', 'maim.views.manu_search'),
    url(r'^nutrinfo/$','maim.views.nutrinfo'),
    url(r'^cereal_list2/$','maim.views.cereal_list2'),
    url(r'^cereal_detail/(?P<pk>\d+)/$','maim.views.cereal_detail'),
    url(r'^form_view/$','maim.views.form_view'),
    url(r'^form_view2/$','maim.views.form_view2'),
    url(r'^cereal_create/$','maim.views.cereal_create'),
    url(r'^signup/$','maim.views.signup'),
    url(r'^home/$','maim.views.home'),
    url(r'^signin/$','maim.views.signin'),
    url(r'^logout/$','maim.views.logout_view'),







] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

"""jobTracker URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
import apps.jobTrackerWebapp.urls as rest_urls
import apps.jobTrackerWebapp.views as views

# import apps.settings as settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^view_jobs', views.mongo_view_all_jobs, name="view_all_jobs"),
    # url(r'^static/(?P<path>.*)$', django.contrib.staticfiles),
    url(r'^admin/', admin.site.urls),
    url(r'^rest/', include(rest_urls), name='rest_urls')
]

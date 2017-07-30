"""data_entery_ui URL Configuration

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
from django.contrib import admin
from add_data.views import (AddDataToDb, ListData, GetMyIp, AddTaskToDb, 
                                TaskListData, AddPreferenceView, AddAspirationListData,
                                AddAspirationToDb, AddAspirationPreferenceView)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', AddDataToDb.as_view(), name="post_data"),
    url(r'^list$', ListData.as_view(), name="list_data"),
    url(r'^knowmyip$', GetMyIp.as_view(), name="know_my_ip"),
    url(r'^add/task$', AddTaskToDb.as_view(), name="add_task"),
    url(r'^task/list$', TaskListData.as_view(), name="list_data"),
    url(r'^add/(?P<pk>\d+)/preference$', AddPreferenceView.as_view(), name="add_preferance"),
    url(r'^aspiration$', AddAspirationToDb.as_view(), name="Aspirations_data"),
    url(r'^aspiration/(?P<pk>\d+)/preference$', AddAspirationPreferenceView.as_view(), name="add_aspiration_preferance"),
    url(r'^aspiration/list$', AddAspirationListData.as_view(), name="aspiration_list_data"),







]

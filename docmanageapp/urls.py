"""docmanageapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required

from initial.views import login_view, logout_view, home_view
from menu.views import MenuView
from download.views import DownloadView, DownloadTableView, document_json
from upload.views import UploadView, single_upload

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('menu', login_required(MenuView.as_view()), name='menu'),
    path('upload', login_required(UploadView.as_view()), name='upload'),
    path('single-upload', single_upload, name='single-upload'),
    path('download', login_required(DownloadView.as_view()), name='download'),
    path('download-table', login_required(DownloadTableView.as_view()), name='download_table'),
    path('document/json/', document_json, name='doc_json'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
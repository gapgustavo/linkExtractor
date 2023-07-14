from django.contrib import admin
from django.urls import path, include
from search.api.apiviews import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', include('search.urls')),
    path('searchapi/', SearchView.as_view(), name='searchapi'), #API
    path('searchapi/doc', searchApiDoc, name="searchapidoc")
]

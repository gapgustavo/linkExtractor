from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('do_search/', views.do_search, name="do_search"),
    path('search_done/', views.search_done, name="search_done"),
    path('history/', views.history, name="history"),
    path('delete_history/<int:id>', views.delete_history, name="delete_history"),
    path('access_search/<int:id>', views.access_search, name="access_search"),
]
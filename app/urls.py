from . import views, api
from django.urls import path
urlpatterns = [
    path('', views.home, name='home'),
    path('data/', views.dht11, name='Data'),
    path('api/list', api.Dlist, name='DHT11List'),
    path('api/post', api.dhtviews.as_view(), name='DHT_post'),
]

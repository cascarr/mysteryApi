from django.urls import path 
from rest_framework.urlpatterns import format_suffix_patterns 
from . import views 

name = 'apiapp'
urlpatterns = [
    path('items/', views.ItemView.as_view(), name='item-view'),
    path('items/<int:pk>/', views.ItemDetail.as_view(), name='item-detail'),
    path('', views.home, name='home'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
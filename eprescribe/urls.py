from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,  name='home'),
    path('createform/', views.createprescribe, name='createform'),
    path('updateprescribe/<int:id>/', views.updateprescribe, name='updateprescribe'),
    path('delete/<int:id>/', views.deletemed, name='delete'),
    path('detailmed/<int:id>/', views.detailmed, name='detailmed')
]

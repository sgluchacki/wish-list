from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('wish/create/', views.WishCreate.as_view(), name='wish_create'),
    path('wish/<int:pk>/delete/', views.WishDelete.as_view(), name='wish_delete'),
]
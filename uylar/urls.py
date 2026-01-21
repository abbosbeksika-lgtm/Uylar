from django.urls import path
from . import views

urlpatterns = [
    path('', views.HouseListView.as_view(), name='index'),
    path('detail/<int:pk>/', views.HouseDetailView.as_view(), name='detail'),
    path('create/', views.HouseCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.HouseUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.HouseDeleteView.as_view(), name='delete'),
]

from django.urls import path
from .views import ShowListView, ShowDetailView 

urlpatterns = [
    path('shows/', ShowListView.as_view(), name='show_list'),
    path('shows/<slug:id>', ShowDetailView.as_view(), name='show_detail'),
]
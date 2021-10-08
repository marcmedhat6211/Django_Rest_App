from django.urls import path
from .views import article_detail, article_list

urlpatterns = [
    path('article/', article_list),
    path('article/details/<int:pk>/', article_detail),
]
from django.urls import path
from .views import ArticleDetails, GenericAPIView, article_detail, article_list, ArticleAPIView

urlpatterns = [
    # path('article/', article_list),
    path('article/', ArticleAPIView.as_view()),
    # path('article/details/<int:pk>/', article_detail),
    path('article/details/<int:id>/', ArticleDetails.as_view()),
    path('generic/article/<int:id>', GenericAPIView.as_view()),
    # path('generic/article/<int:id>', GenericAPIView.as_view())
]
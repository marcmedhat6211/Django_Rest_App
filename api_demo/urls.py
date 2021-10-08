from django.urls import path
from django.urls.conf import include
from .views import ArticleDetails, GenericAPIView, article_detail, article_list, ArticleAPIView, ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename = 'article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),

    # path('article/', article_list),
    path('article/', ArticleAPIView.as_view()),
    # path('article/details/<int:pk>/', article_detail),
    path('article/details/<int:id>/', ArticleDetails.as_view()),
    path('generic/article/<int:id>', GenericAPIView.as_view()),
    # path('generic/article/<int:id>', GenericAPIView.as_view())
]
from django.urls import path
from news.api.views import (ArticleListCreateAPIView,
                            ArticleDetailAPIView,
                            JournalistListCreateAPIView)
# from news.api.views import (article_list_create_api_view,
#                             article_detail_api_view)

urlpatterns = [
    path("articles/",
         ArticleListCreateAPIView.as_view(),
         name="article-list"),

    path("articles/<int:pk>/",
         ArticleDetailAPIView.as_view(),
         name="article-detail"),

    path("journalists/",
         JournalistListCreateAPIView.as_view(),
         name="journalist-list")
]

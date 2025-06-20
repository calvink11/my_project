from django.urls import path
from app_latest_news_browse import views

app_name = "app_latest_news_browse"

urlpatterns = [
    path('', views.home, name="home"),
    path("api_query_keyword_cate_news/", views.api_query_keyword_cate_news),
    path("api_news_content/", views.api_news_content),
]

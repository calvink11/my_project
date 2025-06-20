"""website_configs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('topword/', include('app_top_keyword.urls')),
    path('topperson/', include('app_top_person.urls')),
    path('', include('app_top_ner.urls')),
    path('userkeyword/', include('app_user_keyword.urls')),
    path('userkeyword_assoc/', include('app_user_keyword_association.urls')),
    path('userkeyword_senti/', include('app_user_keyword_sentiment.urls')),
    path('toppersonYesterday/', include('app_top_person_yesterday.urls')),
    path('scchen/', include('app_scchen.urls')),
    path('correlation/', include('app_correlation.urls')),
    path('taipeimayor/', include('app_taipei_mayor.urls')),
    path("newsrcmd/", include('app_news_rcmd_bert.urls')),
    path('sentiment/', include('app_sentiment_bert.urls')),
    path('classification/', include('app_news_classification_bert.urls')),
    path('latestnews', include('app_latest_news_browse.urls'))
]

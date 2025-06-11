# News URLs configuration - default path is the index page
from django.urls import path
from news.views import news_list, news_detail

app_name = "news"

urlpatterns = [
    path("", news_list, name="news_list"),
    path("<int:pk>/", news_detail, name="news_detail"),
]

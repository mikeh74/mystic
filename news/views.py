from django.shortcuts import render

# Create the views for the news app
from django.views.generic import ListView, DetailView
from news.models import News


class NewsListView(ListView):
    model = News
    template_name = "news/news_list.html"
    context_object_name = "news_list"
    paginate_by = 10  # Number of news items per page
    ordering = ["-published_date"]  # Order by published date, newest first    

    def get_queryset(self):
        return News.objects.all()


class NewsDetailView(DetailView):
    model = News
    template_name = "news/news_detail.html"
    context_object_name = "news_item"

    def get_queryset(self):
        return News.objects.all()

from django.shortcuts import render, get_object_or_404
from news.models import News


def news_list(request):
    news_list = News.objects.all()
    page = request.GET.get("page", 1)
    paginate_by = 10
    start = (int(page) - 1) * paginate_by
    end = start + paginate_by
 
    # Get selected categories from the request
    selected_category = request.GET.get("category")
    if selected_category:
        news_list = news_list.filter(category=selected_category)

    context = {
        "news_list": news_list[start:end],
    }

    return render(
        request,
        "news/news_list.html",
        context,
    )


def news_detail(request, pk):
    context = {}
    return render(
        request,
        "news/news_detail.html",
        context,
    )

from django.contrib import admin
from news.models import News


# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "published_date", "author")
    search_fields = ("title", "article", "author")
    list_filter = ("published_date",)
    date_hierarchy = "published_date"
    ordering = ("-published_date",)

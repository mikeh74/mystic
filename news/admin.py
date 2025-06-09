from django.contrib import admin
from news.models import News, Category


# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "published_date", "author")
    search_fields = ("title", "article", "author")
    list_filter = ("published_date",)
    date_hierarchy = "published_date"
    ordering = ("-published_date",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)

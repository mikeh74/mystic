from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class News(models.Model):
    title = models.CharField(max_length=200)
    article = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="news_images/", blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="news_items",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-published_date"]
        verbose_name = "News"
        verbose_name_plural = "News"

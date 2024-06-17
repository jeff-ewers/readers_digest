from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=155)
    author = models.CharField(max_length=155)
    cover_image = models.CharField(max_length=155)
    isbn = models.CharField(max_length=155)
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(
        "Category",
        through='BookCategory',
        related_name="book_categories"
    )

from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    category = models.CharField(max_length=160)
    books = models.ManyToManyField(
        "Book",
        through='BookCategory',
        related_name="category_books"
    )
from django.db import models


class BookCategory(models.Model):
    book_id = models.ForeignKey("Book", on_delete=models.CASCADE)
    category_id = models.ForeignKey("Category", on_delete=models.CASCADE)

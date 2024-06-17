from django.db import models
from django.contrib.auth.models import User



class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collection')
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name='book')
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    comment = models.CharField(max_length=155)
    created_at = models.DateTimeField(auto_now_add=True)

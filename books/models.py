
from django_cryptography.fields import encrypt
from django.db import models
from django.urls import reverse

class Book(models.Model):
    title = encrypt(models.CharField(max_length=200))
    author = encrypt(models.CharField(max_length = 200))
    description = encrypt(models.CharField(max_length = 500, default=None))
    price = encrypt(models.FloatField(null=True, blank=True))
    image_url = encrypt(models.CharField(max_length = 2083, default=False))
    follow_author = encrypt(models.CharField(max_length=2083, blank=True))  
    book_available = encrypt(models.BooleanField(default=False))

    def __str__(self):
        return self.title


class Order(models.Model):
	product = models.ForeignKey(Book, max_length=200, null=True, blank=True, on_delete = models.SET_NULL)
	created =  models.DateTimeField(auto_now_add=True) 

	def __str__(self):
		return self.product.title

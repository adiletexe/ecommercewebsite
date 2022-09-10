from django.db import models
from categories.models import Categories
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    images = models.ImageField(upload_to='static/images')
    price = models.IntegerField()
    stock = models.IntegerField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('product_details', args=[self.category.slug, self.slug])

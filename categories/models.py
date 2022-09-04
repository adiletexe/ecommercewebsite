from django.db import models

# Create your models here.
class Categories(models.Model):
    title = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(max_length=40, unique=True, null=True)
    description = models.TextField(max_length=200)
    image = models.ImageField(blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
from django.db import models
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True)
    price = models.FloatField()
    product_images = models.ImageField(blank=True, upload_to='images/')
    stock = models.PositiveIntegerField()

    # required

    is_available = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created_date',)

    def get_absolute_url(self):
        return reverse("store:product_detail", args=[self.slug])

    def __str__(self):
        return self.product_name

    REQUIRED_FIELDS = ['category', 'product_name',
                       'description', 'price', 'product_images', 'slug']


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse("store:category_list", args=[self.slug])

    def __str__(self):
        return self.name

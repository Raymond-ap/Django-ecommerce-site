from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class DailyOffer(models.Model):
    offer = models.CharField(max_length=150, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.offer


class Category(models.Model):
    category = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['-created']

    def __str__(self):
        return self.category


class Product(models.Model):
    name = models.CharField(max_length=300)
    thumbnail = models.ImageField(upload_to='products_image')
    description = RichTextField()
    price = models.DecimalField(max_digits=100000, decimal_places=2)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    addition_image = models.ImageField(upload_to='products_image')
    published = models.BooleanField(default=True)
    sale = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.item.name

    @property
    def getTotalPrice(self):
        return self.item.price * self.quantity


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username}'


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.user.username

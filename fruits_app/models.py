from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone  # Import timezone for correct datetime handling

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True, null=True)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)  # Use timezone.now for default

    def __str__(self):
        return self.subject

class Blog(models.Model):
    image = models.ImageField(upload_to='uploads/')
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when created

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ManyToManyField(Category, blank=True, related_name='products')  # Use plural for related_name
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    name = models.CharField(max_length=225)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Comment(models.Model):
    name = models.CharField(max_length=225)
    message = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now) 
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey("Author", on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=2, decimal_places=2)
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    category = models.ManyToManyField(Category)
    STATUS_CHOICES = [
        ("IS", "In Stock"),
        ("OS", "Out of Stock"),
        ("O", "On sale"),
        ("N", "New")
    ]
    availability = models.CharField(max_length=50, choices=STATUS_CHOICES)
    FORMAT_CHOICES = [
        ("S", "Standard"),
        ("D", "Downloadable"),
        ("E", "External")
    ]
    format = models.CharField(max_length=50, choices=FORMAT_CHOICES)
    published_date = models.DateField()


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    text = models.TextField()
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])







from django.contrib import admin
from .models import Book, Category, Author, Review


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "price", "rating", "availability", "format", "published_date"]
    search_fields = ["title", "author"]
    filter_horizontal = ["category"]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name", "bio"]
    search_fields = ["name"]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["book", "user", "text", "rating"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    search_fields = ["name"]


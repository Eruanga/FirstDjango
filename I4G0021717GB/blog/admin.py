from django.contrib import admin

# Register your models here.
from blog.models import Author, Post

admin.site.register(Author)
admin.site.register(Post)
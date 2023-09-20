from django.contrib import admin
from .models import Post, Category
# Register your models here.
from .models import Post
admin.site.register(Post)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
admin.site.register(Category, CategoryAdmin)
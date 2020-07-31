from django.contrib import admin

from blog.models import Category, Post, Product
from user.models import Profile


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent')
    prepopulated_fields = {'slug': ('name', )}


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'name', 'created_date', 'update_date', 'product', 'category', 'to_display', 'for_auth')
    list_filter = ('product', 'created_date', 'category')
    list_editable = ('name', 'to_display', 'for_auth')
    prepopulated_fields = {'slug': ('name', )}


class ProductAdmin(admin.ModelAdmin):
    list_display = ('author', 'name', 'created_date', 'tag', 'to_display', 'for_auth')
    list_filter = ('created_date', 'tag')
    list_editable = ('name', 'to_display', 'for_auth')
    prepopulated_fields = {'slug': ('name', )}


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('slug', 'user_id', 'created_date')
    prepopulated_fields = {'slug': ('user', )}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Profile, ProfileAdmin)

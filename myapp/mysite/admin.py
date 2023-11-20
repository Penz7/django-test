from django.contrib import admin
from .models import User, Product
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password')
    search_fields = ("username",)
    list_filter = ('username',)
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('price',)

admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
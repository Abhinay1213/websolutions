from django.contrib import admin
from .models import Vendor,Product
from .models import CustomUser, Wishlist

class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'product')  # Display these fields in the admin list view

# Register the Vendor model and its admin class
admin.site.register(Vendor, VendorAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')  # Display these fields in the admin list view


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email')

# Register the Product model and its admin class
admin.site.register(Product, ProductAdmin)
admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Wishlist)

from django.contrib import admin
from .models import Material, Category

# Register your models here.

class MaterialAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )
    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Material, MaterialAdmin)
admin.site.register(Category, CategoryAdmin)

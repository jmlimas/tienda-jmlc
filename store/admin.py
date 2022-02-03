from django.contrib import admin
from .models import Product, Variation

# Register your models here.
class ProductosAdmin(admin.ModelAdmin):
    list_display = ('id','product_name','price','stock','category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}

class VariationAdmin(admin.ModelAdmin):
    list_display = ('id','product','product_id','variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    lister_filter = ('product' ,' variation_category', 'variation_value', 'is_active')

admin.site.register(Product,ProductosAdmin)
admin.site.register(Variation,VariationAdmin)

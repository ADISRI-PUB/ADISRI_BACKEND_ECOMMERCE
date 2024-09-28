from django.contrib import admin

# Register your models here.
from .models import Product,Book,Pamplate


class PamphletAdmin(admin.ModelAdmin):
    list_display = ('Name',)  # Display the pamphlet name in the list view
    filter_horizontal = ('Products',)  # Use a filter widget for many-to-many field

admin.site.register(Pamplate, PamphletAdmin)

admin.site.register(Product)
admin.site.register(Book)


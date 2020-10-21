# Register Items model in admin

# Django
from django.contrib import admin

# Models
from items.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'picture', 'tags', 'classification',)
    search_fields = ('user__username', 'user__first_name', 'title', 'tags', 'classification', 'price',)
    list_filter = ('created', 'modified', 'price', 'classification',)

    readonly_fields = ('created', 'modified')

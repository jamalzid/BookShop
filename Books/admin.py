from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category',
                    'price', 'days_since_published')
    list_filter = ('user', 'category', 'price', 'published_at')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    actions = ('set_price_to_100',)

    def set_price_to_100(self, request, queryset):
        queryset.update(price=100)
        self.message_user(request, 'price has been changed successfully ')

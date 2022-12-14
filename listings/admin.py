from django.contrib import admin
from .models import Category, Game


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id',)
    list_editable = ('title',)
    list_filter = ('title',)
    list_per_page = 5
    search_fields = ('title',)

admin.site.register(Category, CategoryAdmin)


class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'author', 'title', 'country', 'price',
                    'price_free', 'RAM', 'is_published', 'list_date')
    list_display_links = ('id', 'title')
    list_filter = ('category', 'country', 'price', 'list_date')
    list_editable = ('is_published',)

    search_fields = ('category', 'author', 'title')
    list_per_page = 4

admin.site.register(Game, GameAdmin)



from django.contrib import admin
from .models import Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'is_mvp', 'created_at')
    list_editable = ('email', 'is_mvp')
    list_per_page = 5
    search_fields = ('name',)
    list_display_links = ('id', 'name')
    list_filter = ('name', 'is_mvp', 'created_at')
admin.site.register(Company, CompanyAdmin)


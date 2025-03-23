from django.contrib import admin

from .models import Category , Product , File



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['parent', 'title', 'is_enabled', 'create_time']
    list_filter = ['parent','is_enabled']
    search_fields = ['title']


class FileInLineAdmin(admin.StackedInline):
    model = File
    fields = ['title', 'file','is_enabled']
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title',  'create_time']
    list_filter = ['is_enabled']
    filter_horizontal = ['categories']
    search_fields = ['title']
    inlines = [FileInLineAdmin]


# admin.site.register(Product, ProductAdmin)
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(File, FileInLineAdmin)

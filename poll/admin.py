from django.contrib import admin
from .models import  *

# Register your models here.


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'created_at')
    search_fields = ('name',)
    list_filter = ('name',)
    #list_editable = ('created_at',)
    ordering = ('-id',)
    fields = ('name', 'address', 'created_at')
    class Meta:
        model = Publisher

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)
    list_filter = ('name',)
    #list_editable = ('created_at',)
    ordering = ('-id',)
    fields = ('name', 'created_at')
    class Meta:
        model = Category

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','publisher','isbn', 'category', 'pages', 'publish_at', 'created_at')
    search_fields = ('name','publisher')
    list_filter = ('category', 'publisher')
    #list_display_links = ('phone',)
    list_editable = ('publisher',)
    ordering = ('-id',)
    fields = ('name', 'isbn', 'pages')
    class Meta:
        model = Book
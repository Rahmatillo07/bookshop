from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Book, User, Cart


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id','category','get_photo','title','price','author','date_created','discount']
    list_display_links = ['id','title']
    list_editable = ['category','price','discount']

    def get_photo(self,obj):
        return mark_safe(f'<img src="{obj.image.url if obj.image else None}" width="75">')


admin.site.register(User)


admin.site.register(Category)
admin.site.register(Cart)








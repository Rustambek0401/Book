from django.contrib import admin
from import_export.admin import ImportExportMixin

from book.models import Category,Book,Author
# Register your models here.


@admin.register(Category)
class CustomerModelAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('category_name','slug')


@admin.register(Book)
class CustomerModelAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('book_name','description','price','quantity','rating','slug')

@admin.register(Author)
class CustomerModelAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('full_name','phone','adress','email','slug')

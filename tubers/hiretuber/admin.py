from django.contrib import admin
from .models import Hiretuber
from django.utils.html import format_html

class HiretubersAdmin(admin.ModelAdmin):

    list_display = ('first_name','last_name','tuber_name')
    list_display_links = ('first_name','last_name','tuber_name')

# Register your models here.

admin.site.register(Hiretuber,HiretubersAdmin)

from django.contrib import admin
from .models import Youtuber
from django.utils.html import format_html

# Register your models here.


class YoutubersAdmin(admin.ModelAdmin):

    def youTuberPhoto(self,object):
        return format_html('<img src ="{}" width = "70"/>'.format(object.photo.url))


    list_display = ('id','youTuberPhoto','name', 'price', 'camera_type','is_featured')
    list_display_links = ('id','name','camera_type')
    search_fields = ('camera_type','crew', 'city')
    list_filter = ('city','camera_type')
    list_editable = ('is_featured',)

admin.site.register(Youtuber,YoutubersAdmin)
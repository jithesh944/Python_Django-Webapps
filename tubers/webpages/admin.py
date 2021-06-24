from django.contrib import admin
from .models import Slider, Team
from django.utils.html import format_html

class TeamAdmin(admin.ModelAdmin):

    def myphoto(self,object):
        return format_html('<img src ="{}" width = "40"/>'.format(object.photo.url))


    list_display = ('id','myphoto','first_name','role','created_date')
    list_display_links = ('id','first_name')
    search_fields = ('first_name',)
    list_filter = ('role',)

class SliderAdmin(admin.ModelAdmin):
    def slider_photo(self,object):
        return format_html('<img src ="{}" width = "140"/>'.format(object.photo.url))

    list_display = ('headline','slider_photo','button_text')
    list_display_links = ('headline','button_text')
# Register your models here.

admin.site.register(Slider,SliderAdmin)
admin.site.register(Team,TeamAdmin)
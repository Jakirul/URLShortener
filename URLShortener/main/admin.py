from django.contrib import admin
from .models import Main

# class mainAdmin(admin.ModelAdmin):
#     list_display = ('url', 'shortnened_url')

# Register your models here.

# admin.site.register(Main, mainAdmin)
admin.site.register(Main)
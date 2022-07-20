from django.contrib import admin

# Register your models here.

from .models import Foundation,Description

admin.site.register(Foundation)
admin.site.register(Description)

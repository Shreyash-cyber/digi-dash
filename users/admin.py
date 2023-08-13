from django.contrib import admin
from .models import *

from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class JsonResource(resources.ModelResource):
    class Meta:
        model = Jsondata

class Jsonadmin(ImportExportModelAdmin):
    resource_class = JsonResource
    
admin.site.register(Profile)
admin.site.register(Jsondata, Jsonadmin)
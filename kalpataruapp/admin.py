from django.contrib import admin
from .models import Plant
'''
class PlantAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price']
    list_editable = ['price']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Plant, PlantAdmin)'''

class PlantAdmin(admin.ModelAdmin):
    list_display = ['name','price']
    list_editable = ['price']
    
admin.site.register(Plant, PlantAdmin)


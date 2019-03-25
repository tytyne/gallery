from django.contrib import admin
from .models import Editor,Image,Location,Category
# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('editor',)

admin.site.register(Editor)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Image,ImageAdmin)

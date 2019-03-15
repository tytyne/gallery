from django.contrib import admin
from .models import Editor,Article,Location,Category
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('location',)

admin.site.register(Editor)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Article,ArticleAdmin)

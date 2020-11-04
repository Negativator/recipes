from django.contrib import admin

# Register your models here.
from my_recipes.models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


admin.site.register(Recipe, RecipeAdmin)

from csv import list_dialects
from django.contrib import admin
from django.contrib.auth import get_user_model


from .models import Recipe, RecipeIngredient
# Register your models here.
User = get_user_model()
admin.site.unregister(User)

class RecipeInline(admin.StackedInline):
    model = Recipe
    extra = 0
    #fields = ['name', 'quantity', 'unit', 'direction']

class UserAdmin(admin.ModelAdmin):
    inlines = [RecipeInline]
    list_display = ['username']

admin.site.register(User, UserAdmin)

class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    extra = 0
    #fields = ['name', 'quantity', 'unit', 'direction']


class RecipeIngredientOutline(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'unit', 'updated']
    

admin.site.register(RecipeIngredient,RecipeIngredientOutline)

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = ['name', 'user', 'timestamp','updated']
    readonly_fields = ['timestamp', 'updated']
    raw_id_fields = ['user']

admin.site.register(Recipe, RecipeAdmin)


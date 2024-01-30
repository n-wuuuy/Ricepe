from django.contrib import admin

from recipe.models import Product, Recipe, RecipeProduct


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'times_used')
    list_filter = ('times_used',)
    search_fields = ('name', 'id')


class RecipeProductInline(admin.TabularInline):
    model = RecipeProduct
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', 'id')
    inlines = [RecipeProductInline]


@admin.register(RecipeProduct)
class RecipeProductAdmin(admin.ModelAdmin):
    search_fields = ('id', 'weight')

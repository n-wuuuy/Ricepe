from django.db import IntegrityError
from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render

from recipe.models import RecipeProduct, Recipe, Product


# Create your views here.

def add_product_to_recipe(request):
    if request.method == 'GET':
        recipe_id = request.GET.get('recipe_id')
        product_id = request.GET.get('product_id')
        weight = request.GET.get('weight')
        try:
            recipe_product, created = RecipeProduct.objects.get_or_create(recipe_id=recipe_id,
                                                                          product_id=product_id)
            recipe_product.weight = weight
            recipe_product.save()
            return JsonResponse({'status': 'success'})
        except IntegrityError as e:
            return JsonResponse({'status': 'error', 'message': str(e)})


def cook_recipe(request):
    if request.method == 'GET':
        recipe_id = request.GET.get('recipe_id')
        Product.objects.filter(recipe__id=recipe_id).update(times_used=F('times_used') + 1)
        return JsonResponse({'status': 'success'})


def show_recipes_without_product(request):
    if request.method == 'GET':
        product_id = request.GET.get('product_id')
        rp = RecipeProduct.objects.exclude(weight__lte=10).filter(product_id=product_id)
        recipes = Recipe.objects.exclude(recipeproduct__in=rp)
        return render(request, 'recipe/show_recipes_without_product.html', {'recipes': recipes})

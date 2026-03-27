from django.http import HttpResponse
from django.shortcuts import render
from utils.recipes.factory import make_recipe
# from recipes.models import Recipe  # ou 
from .models import Recipe

# Create your views here.
def home(request):
    # recipes = Recipe.objects.all().order_by('-id')
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request,'recipes/pages/home.html', context={
        # 'name': 'Henri Vieira',
#        'recipes': [make_recipe() for _ in range(11)],
        'recipes': recipes,
    })

def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published=True,
    ).order_by('-id')
    return render(request,'recipes/pages/category.html', context={
        # 'name': 'Henri Vieira',
#        'recipes': [make_recipe() for _ in range(11)],
        'recipes': recipes,
    })

def recipe(request, id):
    return render(request,'recipes/pages/recipe-view.html', context={
        # 'name': 'Henri Vieira',
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
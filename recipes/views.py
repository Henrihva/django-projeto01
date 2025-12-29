from django.http import HttpResponse
from django.shortcuts import render
from utils.recipes.factory import make_recipe

# Create your views here.
def home(request):
    return render(request,'recipes/pages/home.html', context={
        # 'name': 'Henri Vieira',
        'recipes': [make_recipe() for _ in range(11)],
    })

def recipe(request, id):
    return render(request,'recipes/pages/recipe-view.html', context={
        # 'name': 'Henri Vieira',
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
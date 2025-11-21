from django.urls import path

# from recipes.views import my_home #, my_sobre, my_contato
#  from recipes import views
from . import views

urlpatterns = [

    path('', views.home),
    # path('recipes/', views.recipe),
    path('recipes/<int:id>/', views.recipe),
    # path('sobre/',my_sobre),
    # path('contato/',my_contato),
]
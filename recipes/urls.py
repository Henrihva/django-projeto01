from django.urls import path

from recipes.views import my_home #, my_sobre, my_contato

urlpatterns = [
    path('',my_home),
    # path('sobre/',my_sobre),
    # path('contato/',my_contato),
]
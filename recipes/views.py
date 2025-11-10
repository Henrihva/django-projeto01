from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def my_home(request):
    # return http response 
    # return HttpResponse('Pagina INICIAL alterada...!!!')
    return render(request,'recipes/home.html')

def my_sobre(request):
    # return http response 
    return HttpResponse('pagina Sobre ...!!!')

def my_contato(request):
    # return http response 
    return HttpResponse('Página Contatos ...!!!')
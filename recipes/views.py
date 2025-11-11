from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def my_home(request):
    # return http response 
    # return HttpResponse('Pagina INICIAL alterada...!!!')
    return render(request,'recipes/pages/home.html', context={
        'name': 'Henri Vieira',
    })

# def my_sobre(request):
#     # return http response 
#     return HttpResponse('pagina Sobre ...!!!')

# def my_contato(request):
#     # return http response 
#     return HttpResponse('Página Contatos ...!!!')
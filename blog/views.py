from django.shortcuts import render
from .models import Cadastro


def post_list(request):
    variavel = Cadastro.objects.all()
    return render(request, 'post_list.html',{'variavel':variavel})



from django.shortcuts import render

# Create your views here.


def usuarios(request):
    return render(request, "pruebaclase1/usuarios.html")

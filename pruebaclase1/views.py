from django.shortcuts import render, HttpResponse
from form
# Create your views here.


def usuarios(request):
    return render(request, "pruebaclase1/usuarios.html")

def contact(request):
    if request.method == 'POST':
        name= request.POST.get('nombre', '')
        return HttpResponse(f"el nombre del formulario es {name}")
    return render (request, 'pruebaclase1/contact.html')

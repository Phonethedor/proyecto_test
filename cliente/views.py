from django.shortcuts import render, HttpResponse
from .models import Cliente

# Create your views here.
def inicio(request):
    # return HttpResponse("op") con esto seria respuesta directa
    return render(request, "index.html") #con esto redireccionaria a un html predefinido en la carpeta templates

def agregar(request):
    # capturar parametros enviados por el formulario en html variable  = request.post['parametro']
    Cliente.objects.create(
    nombre = request.POST['nombre'],
    apellido = request.POST['apellido'],
    rut = request.POST['rut'],
    email = request.POST['email'],
    password = request.POST['password']
    )
    return render(request,"index.html")

def leer(request):
    clientes = Cliente.objects.all()
    return render(request,"index.html")

def actualizar(request):
    id = request.POST['id']
    cliente = Cliente.objects.get(id=id) # trae el id
    errors = Cliente.objects.validador_cliente(request.POST) # ya que se valida por POST

    
    if len(cliente) > 0: # verifica que traiga dato
        cliente.nombre = request.POST['nombre']
        cliente.apellido = request.POST['apellido']
        cliente.rut = request.POST['rut']
        cliente.email = request.POST['email']
        cliente.password = request.POST['password']
    return


def borrar(request):

    pass

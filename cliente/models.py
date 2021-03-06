from django.db import models
import re

# Create your models here.
class ClienteManager(models.Manager): # se define el manager de cliente
    def validador_cliente(self, data):
        errors = {}
        if len(data['nombre']) == 0:
            errors['nombre'] = 'Ingrese un nombre'
        if len(data['apellido']) == 0:
            errors['apellido'] = 'Ingrese un apellido'
        if len(data['rut']) == 0:
            errors['rut'] = 'Ingrese rut'
        EMAIL = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') # requiere importar re
        if not EMAIL.match(data['email']): # utilizaba datos recurrentes
            errors['email'] = "email invalido"
        # if len(data['password']) == 0:
        #    errors['password'] = 'Ingrese password'
        # la validacion de pass no se considerara esta ves
        return errors


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=12)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ClienteManager() # se crea el manager de cliente
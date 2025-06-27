from django.db import models
from django.contrib.auth.hashers import make_password # Es para hashear contraseñas
from django.utils import timezone # Para manejar fechas y horas


class User(models.Model):
    """ Modelo Usuario para el CRM """
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    es_administrador = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # hashear la contraseña solo si es un nuevo usuario 
        if not self.pk:  
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre
    
    
class Company(models.Model):
    """ Modelo Compañía para el CRM """
    nombre = models.CharField(max_length=150)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Compañía"
        verbose_name_plural = "Compañías"

class Customer(models.Model):
    """ Modelo Cliente para el CRM """
    nombre = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField()
    compania = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='clientes')
    representante = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clientes')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

class Interaction(models.Model):
    """ Modelo Interacción para el CRM """
    TIPOS_INTERACCION = [
        ('Llamada', 'Llamada'),
        ('Correo Electronico', 'Correo Electrónico'),
        ('SMS', 'SMS'),
        ('Facebook', 'Facebook'),
        ('WhatsApp', 'WhatsApp'),
        ('Otro', 'Otro'), # Agregué "Otro" como opción para mayor flexibilidad
    ]

    cliente = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='interacciones')
    tipo_interaccion = models.CharField(max_length=50, choices=TIPOS_INTERACCION) # Aumenté el max_length para tipos más largos
    fecha_interaccion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.cliente.nombre} - {self.tipo_interaccion}"

    class Meta:
        verbose_name = "Interacción"
        verbose_name_plural = "Interacciones"
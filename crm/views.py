from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
from datetime import datetime, timedelta
from django.utils import timezone
from .models import Customer, Interaction


class ListaClientes(ListView):

    model = Customer
    template_name = 'crm/lista_clientes_simple.html'
    context_object_name = 'clientes'
    paginate_by = 10  # Mostrar 10 clientes por página
    
    def get_queryset(self):
        # Obtener todos los clientes
        clientes = Customer.objects.all()
        
        # Filtro por nombre
        nombre_buscar = self.request.GET.get('buscar')
        if nombre_buscar:
            clientes = clientes.filter(nombre__icontains=nombre_buscar)
        
        # Filtro por cumpleaños
        cumple_filtro = self.request.GET.get('cumpleanos')
        hoy = timezone.now().date()
        
        if cumple_filtro == 'esta_semana':
            clientes = clientes.filter(fecha_nacimiento__month=hoy.month)
        elif cumple_filtro == 'este_mes':
            clientes = clientes.filter(fecha_nacimiento__month=hoy.month)
        
        # Ordenar
        como_ordenar = self.request.GET.get('ordenar', 'nombre')
        
        if como_ordenar == 'nombre':
            clientes = clientes.order_by('nombre')
        elif como_ordenar == 'compania':
            clientes = clientes.order_by('compania__nombre')
        elif como_ordenar == 'cumpleanos':
            clientes = clientes.order_by('fecha_nacimiento')
        
        return clientes
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Pasar los filtros al template
        context['buscar'] = self.request.GET.get('buscar', '')
        context['cumpleanos_filtro'] = self.request.GET.get('cumpleanos', '')
        context['ordenar'] = self.request.GET.get('ordenar', 'nombre')
        
        # Para cada cliente, agregar info extra
        for cliente in context['clientes']:
            
            # Formatear cumpleaños bonito (formato "February 5")
            cliente.cumpleanos_bonito = cliente.fecha_nacimiento.strftime("%B %d")
            
            # Buscar última interacción
            ultima = cliente.interacciones.order_by('-fecha_interaccion').first()
            cliente.ultima_interaccion = ultima
            
            if ultima:
                # Calcular cuánto tiempo pasó
                ahora = timezone.now()
                diferencia = ahora - ultima.fecha_interaccion
                dias_pasados = diferencia.days
                
                # Decidir qué mostrar (formato "1 day ago")
                if dias_pasados == 0:
                    cliente.tiempo = "Today"
                elif dias_pasados == 1:
                    cliente.tiempo = "1 day ago"
                elif dias_pasados < 7:
                    cliente.tiempo = f"{dias_pasados} days ago"
                else:
                    semanas = dias_pasados // 7
                    cliente.tiempo = f"{semanas} weeks ago"
                
                # Tipo de interacción (para mostrar "Phone", "Email", etc.)
                cliente.tipo_interaccion = ultima.tipo_interaccion
            else:
                cliente.tiempo = "No interactions"
                cliente.tipo_interaccion = "None"
                cliente.ultima_interaccion = None
        
        return context

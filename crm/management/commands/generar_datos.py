import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker # Generador de datos ficticios
from crm.models import User, Company, Customer, Interaction # Importar modelos necesarios


class Command(BaseCommand):
    """    Comando para generar datos ficticios en el CRM.
    Crea 3 representantes, 1000 clientes y 500 interacciones por cliente.
    """
    help = 'Genera datos ficticios para el CRM: 3 representantes, 1000 clientes y 500 interacciones por cliente'

    def __init__(self):
        super().__init__()
        self.fake = Faker('es_ES')  # Faker en español

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Elimina todos los datos existentes antes de generar nuevos',
        )

    def handle(self, *args, **options):
        if options['clear']:
            self.stdout.write('Eliminando datos existentes...')
            Interaction.objects.all().delete()
            Customer.objects.all().delete()
            Company.objects.all().delete()
            User.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Datos eliminados exitosamente.'))

        self.stdout.write('Iniciando generación de datos ficticios...')
        
        # Crear 3 representantes (users)
        users = self.create_users()
        
        # Crear compañías
        companies = self.create_companies()
        
        # Crear 1000 clientes
        customers = self.create_customers(users, companies)
        
        # Crear 500 interacciones por cliente (500,000 total)
        self.create_interactions(customers)
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Datos generados exitosamente:\n'
                f'- {len(users)} representantes\n'
                f'- {len(companies)} compañías\n'
                f'- {len(customers)} clientes\n'
                f'- ~500,000 interacciones'
            )
        )

    def create_users(self):
        self.stdout.write('Creando 3 representantes...')
        users = []
        
        nombres_representantes = [
            ('Carlos', 'Rodriguez'),
            ('Maria', 'Garcia'),
            ('Juan', 'Martinez')
        ]
        
        for i, (nombre, apellido) in enumerate(nombres_representantes):
            user = User.objects.create(
                nombre=f"{nombre} {apellido}",
                correo_electronico=f"{nombre.lower()}.{apellido.lower()}@empresa.com",
                password="password123",  # Se hasheará automáticamente en el modelo
                es_administrador=(i == 0)  # El primero será administrador
            )
            users.append(user)
            
        self.stdout.write(f'✓ Creados {len(users)} representantes')
        return users

    def create_companies(self):
        self.stdout.write('Creando compañías...')
        companies = []
        
        # Nombres de compañías realistas
        nombres_companias = [
            'Tecnología Avanzada S.A.',
            'Soluciones Empresariales Ltd.',
            'Innovación Digital Corp.',
            'Servicios Profesionales S.L.',
            'Consultoría Estratégica S.A.',
            'Desarrollo de Software Inc.',
            'Marketing Digital Pro',
            'Automatización Industrial',
            'Sistemas Inteligentes S.A.',
            'Comercio Electrónico Plus',
            'Logística Integral S.L.',
            'Recursos Humanos 360',
            'Finanzas Corporativas S.A.',
            'Educación Online Ltd.',
            'Salud Digital Corp.',
            'Energías Renovables S.A.',
            'Construcción Moderna S.L.',
            'Alimentación Gourmet Inc.',
            'Textiles Premium S.A.',
            'Transporte Eficiente Ltd.'
        ]
        
        for nombre in nombres_companias:
            company = Company.objects.create(nombre=nombre)
            companies.append(company)
            
        self.stdout.write(f'✓ Creadas {len(companies)} compañías')
        return companies

    def create_customers(self, users, companies):
        self.stdout.write('Creando 1000 clientes...')
        customers = []
        
        for i in range(1000):
            # Generar fecha de nacimiento aleatoria (entre 18 y 80 años)
            birth_date = self.fake.date_of_birth(minimum_age=18, maximum_age=80)
            
            customer = Customer.objects.create(
                nombre=self.fake.name(),
                fecha_nacimiento=birth_date,
                compania=random.choice(companies),
                representante=random.choice(users)
            )
            customers.append(customer)
            
            # Mostrar progreso cada 100 clientes
            if (i + 1) % 100 == 0:
                self.stdout.write(f'  Procesados {i + 1}/1000 clientes...')
                
        self.stdout.write(f'✓ Creados {len(customers)} clientes')
        return customers

    def create_interactions(self, customers):
        self.stdout.write('Creando ~500,000 interacciones (500 por cliente)...')
        
        tipos_interaccion = [
            'Llamada',
            'Correo Electronico', 
            'SMS',
            'Facebook',
            'WhatsApp',
            'Otro'
        ]
        
        interactions_created = 0
        
        for i, customer in enumerate(customers):
            # Crear 500 interacciones por cliente
            interactions_batch = []
            
            for j in range(500):
                # Fecha aleatoria en los últimos 2 años
                interaction_date = timezone.now() - timedelta(
                    days=random.randint(0, 730),
                    hours=random.randint(0, 23),
                    minutes=random.randint(0, 59)
                )
                
                interaction = Interaction(
                    cliente=customer,
                    tipo_interaccion=random.choice(tipos_interaccion),
                    fecha_interaccion=interaction_date
                )
                interactions_batch.append(interaction)
            
            # Crear las interacciones en lote para mejor rendimiento
            Interaction.objects.bulk_create(interactions_batch)
            interactions_created += 500
            
            # Mostrar progreso cada 50 clientes
            if (i + 1) % 50 == 0:
                self.stdout.write(f'  Procesados {i + 1}/1000 clientes ({interactions_created:,} interacciones)...')
        
        self.stdout.write(f'✓ Creadas {interactions_created:,} interacciones')

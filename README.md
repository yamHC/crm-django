# 🚀 Sistema CRM Django

Un sistema completo de gestión de clientes (CRM) desarrollado en Django que permite administrar representantes de ventas, compañías, clientes e interacciones.

## 📋 Características

- **Gestión de clientes** con información completa
- **Filtros avanzados** por nombre y cumpleaños
- **Ordenamiento** por múltiples criterios
- **Visualización de interacciones** con timestamps
- **Interface moderna** y responsive
- **Datos ficticios** para pruebas (500,000+ registros)

## 🛠️ Requisitos del Sistema

- Python 3.8 o superior
- Django 4.0 o superior
- Git (opcional)

## ⚡ Instalación Rápida

### Paso 1: Clonar o descargar el proyecto
```bash
# Si tienes git instalado
git clone <url-del-repositorio>
cd crm-django

# O simplemente descarga y extrae los archivos
```

### Paso 2: Crear entorno virtual
```bash
# Crear entorno virtual
python -m venv env

# Activar entorno virtual
# En Windows:
env\Scripts\activate
# En Linux/Mac:
source env/bin/activate
```

### Paso 3: Instalar dependencias
```bash
pip install django faker python-dateutil
```

### Paso 4: Configurar la base de datos
```bash
# Crear las migraciones
python manage.py makemigrations

# Aplicar las migraciones
python manage.py migrate
```

## 📊 Poblar con Datos Ficticios

El proyecto incluye un comando personalizado que genera automáticamente:
- **3 representantes de ventas**
- **20 compañías**
- **1,000 clientes**
- **500,000 interacciones**

### Comando para generar datos:
```bash
python manage.py generar_datos
```

### Comando para limpiar y regenerar datos:
```bash
python manage.py generar_datos --clear
```

**⏱️ Tiempo estimado:** 2-3 minutos para generar todos los datos

## 🎯 Ejecutar el Proyecto

### Iniciar el servidor de desarrollo:
```bash
python manage.py runserver
```

### Acceder a la aplicación:
- **Página principal (CRM):** http://127.0.0.1:8000/
- **Panel de administración:** http://127.0.0.1:8000/admin/

## 🎮 Cómo Usar el Sistema

### Vista Principal del CRM

La aplicación te permitirá:

1. **Ver lista de clientes** con:
   - Nombre completo
   - Compañía
   - Cumpleaños (formato "February 5")
   - Última interacción ("1 day ago (Phone)")

2. **Filtrar clientes por:**
   - Nombre (búsqueda de texto)
   - Cumpleaños ("Esta semana", "Este mes")

3. **Ordenar por:**
   - Nombre A-Z
   - Compañía A-Z
   - Fecha de cumpleaños
   - Última interacción

### Navegación:
- **Página principal:** Lista completa de clientes
- **Paginación:** 10 clientes por página
- **Búsqueda en tiempo real:** Filtra mientras escribes

## 📁 Estructura del Proyecto

```
crm-django/
├── crm/                          # Aplicación principal
│   ├── models.py                 # Modelos de datos
│   ├── views.py                  # Lógica de vistas
│   ├── urls.py                   # URLs de la app
│   ├── templates/crm/            # Templates HTML
│   │   └── lista_clientes_simple.html
│   └── management/commands/      # Comandos personalizados
│       └── generar_datos.py      # Generador de datos ficticios
├── crm_project/                  # Configuración del proyecto
│   ├── settings.py               # Configuraciones
│   └── urls.py                   # URLs principales
├── manage.py                     # Comando principal de Django
└── README.md                     # Este archivo
```

## 🗄️ Modelos de Base de Datos

### User (Representantes)
- Nombre
- Email único
- Contraseña cifrada
- Es administrador (boolean)
- Fechas de creación/actualización

### Company (Compañías)
- Nombre
- Fechas de creación/actualización

### Customer (Clientes)
- Nombre completo
- Fecha de nacimiento
- Relación con compañía
- Relación con representante
- Fechas de creación/actualización

### Interaction (Interacciones)
- Cliente asociado
- Tipo (Llamada, Email, SMS, Facebook, WhatsApp, Otro)
- Fecha de la interacción

## 🛡️ Panel de Administración (Opcional)

Para acceder al panel de administración de Django:

1. **Crear superusuario:**
```bash
python manage.py createsuperuser
```

2. **Acceder a:** http://127.0.0.1:8000/admin/

## 🔧 Comandos Útiles

### Desarrollo:
```bash
# Ejecutar servidor
python manage.py runserver

# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Acceder a shell de Django
python manage.py shell
```

### Datos:
```bash
# Generar datos ficticios
python manage.py generar_datos

# Limpiar y regenerar datos
python manage.py generar_datos --clear
```

## 🔗 Subir a Git/GitHub

### Para desarrolladores que quieren subir el proyecto:

1. **Inicializar repositorio Git:**
```bash
git init
git add .
git commit -m "Initial commit: Sistema CRM Django completo"
```

2. **Crear repositorio en GitHub/GitLab** y luego:
```bash
git remote add origin <tu-url-del-repositorio>
git branch -M main
git push -u origin main
```

3. **Archivos excluidos automáticamente:**
- Base de datos (`db.sqlite3`)
- Entorno virtual (`env/`)
- Archivos temporales y cache
- Configuraciones locales

### Para colaboradores que clonan el proyecto:

1. **Clonar repositorio:**
```bash
git clone <url-del-repositorio>
cd crm-django
```

2. **Seguir pasos de instalación** descritos arriba desde el Paso 2

## 🎉 ¡Listo!

Una vez seguidos estos pasos, tendrás un sistema CRM completamente funcional con miles de registros de prueba para explorar todas las funcionalidades.

**¡Disfruta usando tu Sistema CRM!** 🚀

# Django Books API

Una API RESTful para gestionar libros, construida con Django y Docker. Incluye endpoints para crear, listar, actualizar, eliminar y buscar libros, además de documentación automática con Swagger y Redoc.

---

## Tecnologías utilizadas

- **Python 3.11**
- **Django 5.2**
- **Django REST Framework**
- **drf-spectacular** (para documentación OpenAPI)
- **PostgreSQL**
- **Docker & Docker Compose**
- **Pytest** (para testing)

---

## Clonación y configuración

### 1. Clonación del repositorio

Clona el repositorio en tu máquina local y navega a la carpeta del proyecto:

```bash
git clone https://github.com/Diego2442/django-books.git
cd tu_repositorio
```

## Configuración de las Variables de Entorno

### 1. Copia el archivo .env.template y renómbralo como .env
```bash
cp core/.env.template core/.env
```

### 2. Edita el archivo core/.env con tus valores reales. Aquí tienes un ejemplo de cómo debería verse
```bash
SECRET_KEY='sp2n0cfbbqp%)9lxgjc0@1(7*p@qju0!*ct()3c3ml1!x9ynel'
DEBUG=True

DB_NAME=db_name
DB_USER=user_name
DB_PASSWORD=password
DB_HOST=host_local_o_externo
DB_PORT=5432
```

## Inicialización de Docker

```bash
docker-compose run --rm web pytest && docker-compose up -d
```

## Detener Contenedor

```bash
docker-compose down
```

# Endpoints disponibles: API de Libros

### **Libros** (`/api/books/`)

| **Método** | **Endpoint**            | **Descripción**                   |
|------------|-------------------------|-----------------------------------|
| POST       | `/create`               | Crear un nuevo libro              |
| GET        | `/list`                 | Listar todos los libros           |
| PUT        | `/update/<uuid>`        | Actualizar un libro por UUID      |
| DELETE     | `/delete/<uuid>`        | Eliminar un libro por UUID        |
| GET        | `/search`               | Buscar por autor o título         |

---

## 📖 Documentación Swagger y Redoc

Una vez el contenedor esté corriendo, puedes acceder a la documentación interactiva para explorar los endpoints y probar la API:

- **Swagger UI**: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- **Redoc**: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)
- **Esquema OpenAPI**: [http://localhost:8000/schema/](http://localhost:8000/schema/)




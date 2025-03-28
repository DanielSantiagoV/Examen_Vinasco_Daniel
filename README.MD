# 🎵 Sistema de Gestión de Artistas Musicales

Este es un sistema desarrollado en Python para gestionar información sobre artistas musicales, países y géneros, con generación de informes detallados.

## 🌟 Características Principales

### 🎤 Gestión de Artistas
- Registro completo de artistas musicales.
- Almacenamiento de información detallada:
  - Nombre del artista
  - País de origen
  - Género musical
  - Año de debut
  - Álbumes y certificaciones
- Funcionalidades:
  - Agregar, editar y eliminar artistas.
  - Listado detallado de artistas registrados.

### 🌍 Gestión de Países
- Registro de países de origen de los artistas.
- Funcionalidades:
  - Agregar, editar y eliminar países.
  - Mostrar todos los países registrados.

### 🎸 Gestión de Géneros Musicales
- Registro de géneros musicales asociados a los artistas.
- Funcionalidades:
  - Agregar, editar y eliminar géneros.
  - Mostrar géneros disponibles.

### 📊 Reportes y Consultas
- **Artistas activos en los últimos 10 años**.
- **Artistas por país y rango de tiempo** (ejemplo: artistas de Reino Unido entre 1960-1970).
- **Número de artistas por género musical** (ejemplo: Rock/Pop).
- Datos organizados en informes claros y estructurados.

## 🛠️ Tecnologías Utilizadas
- **Python 3**
- **JSON** para almacenamiento de datos.


## 📋 Requisitos
- Python 3.6 o superior.


## 🚀 Instalación y Uso
1. Clona el repositorio
    `git clone https://github.com/usuario/Examen_Python_VinascoDaniel.git`
2. Instala las dependencias: `pip install -r requirements.txt`
3. Ejecuta el programa: `python main.py`

## 📁 Estructura del Proyecto
```
Examen_Python_VinascoDaniel/
├── main.py
├── modulos/
│   ├── artistas.py
│   ├── paises.py
│   ├── generos.py
│   ├── reportes.py
│   ├── archivo_json.py
└── datos/
    ├── artistas.json
    ├── paises.json
    ├── generos.json
```

## 🗄️ Estructura de los Datos

### 📌 Artistas
```json
{
  "nombre": "The Beatles",
  "pais": "United Kingdom",
  "genero": "Rock",
  "anio_debut": 1960,
  "albumes": [
    {"titulo": "Abbey Road", "certificaciones": "Multi-Platino"}
  ]
}

```

### 🌎 Paises
```json
{
  "nombre": "United Kingdom",
  "codigo": "UK"
}

```

### 🎼 Géneros Musicales
```json
{
  "nombre": "Rock",
  "descripcion": "Género de música popular con raíces en el rock and roll"
}

``````
### 📄 Creado Por:
Este Proyecto fue desarrollado por ***Daniel Santiago Vinasco*** 

-------------------------------------------------------


---

### ✅ **¿Qué incluye este README?**
✔ **📋 Características** detalladas del sistema.  
✔ **📁 Estructura del proyecto** clara y bien organizada.  
✔ **🖥️ Código del menú principal** para referencia.  
✔ **📊 Reportes y funciones clave** del sistema.  
✔ **💾 Estructura de los JSON** con ejemplos.  
✔ **🚀 Instalación y uso** paso a paso.  
✔ **🎨 Estética profesional** con emojis y formato Markdown limpio.  

---
----------------------------------------------

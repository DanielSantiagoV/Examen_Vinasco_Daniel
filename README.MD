

==============================================
🎵 LimeWire - Gestión de Artistas Musicales 🎵
==============================================

📌 DESCRIPCIÓN:
LimeWire es un sistema de gestión que permite administrar información de 
artistas musicales, países y géneros musicales, además de generar informes 
detallados sobre la industria musical.

----------------------------------------------
📂 ESTRUCTURA DEL PROYECTO
----------------------------------------------
Examen_Vinasco_Daniel/
│── data/                     -> Archivos JSON con la información del sistema
│   ├── artistas.json         -> Datos de artistas musicales
│   ├── paises.json           -> Datos de países
│   ├── generos.json          -> Datos de géneros musicales
│── modulos/                  -> Código modularizado
│   ├── artistas.py           -> Gestión de artistas
│   ├── paises.py             -> Gestión de países
│   ├── generos.py            -> Gestión de géneros musicales
│   ├── reportes.py           -> Generación de informes
│   ├── archivo_json.py       -> Funciones para manejar archivos JSON
│── main.py                   -> Archivo principal de ejecución
│── README.txt                -> Documentación del proyecto

----------------------------------------------
🛠 FUNCIONALIDADES
----------------------------------------------
🎤 GESTIÓN DE ARTISTAS:
✔ Agregar, mostrar, editar y eliminar artistas musicales.
✔ Información detallada: país, género, unidades vendidas, estado activo.

🌍 GESTIÓN DE PAÍSES:
✔ Registro de países con códigos ISO y ISO3.
✔ Modificar y eliminar países registrados.

🎼 GESTIÓN DE GÉNEROS MUSICALES:
✔ Registrar nuevos géneros musicales.
✔ Modificar y eliminar géneros existentes.

📊 REPORTES E INFORMES:
✔ Obtener artistas por país y periodo de tiempo.
✔ Listar artistas por género musical.
✔ Reporte de artistas activos en los últimos 10 años.
✔ Contar número de artistas por año de lanzamiento.
✔ Unidades certificadas totales en 2023.

----------------------------------------------
🚀 INSTALACIÓN Y EJECUCIÓN
----------------------------------------------
1. Ejecutar el programa:
    python main.py

----------------------------------------------
📌 REQUISITOS
----------------------------------------------
✔ Python 3.x
✔ Librerías estándar (`json`, `os`, `datetime`)

----------------------------------------------
✅ Elaborado por : Daniel Santiago 

----------------------------------------------

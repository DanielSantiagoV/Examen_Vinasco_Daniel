from modulos.archivo_json import cargar_datos, guardar_datos

GENEROS_JSON = "data/generos.json"

def agregar_genero():
    """Agrega un nuevo género musical."""
    generos = cargar_datos(GENEROS_JSON)

    id_genero = input("ID del género: ").strip()
    descripcion = input("Descripción del género: ").strip()

    nuevo_genero = {"ID": id_genero, "Description": descripcion}

    generos.append(nuevo_genero)
    guardar_datos(GENEROS_JSON, generos)
    print("✅ Género agregado correctamente.")

def mostrar_generos():
    """Muestra la lista de géneros musicales registrados."""
    generos = cargar_datos(GENEROS_JSON)
    
    if not generos:
        print("⚠ No hay géneros registrados.")
        return

    print("\n🎼 Lista de Géneros Musicales:")
    for genero in generos:
        print(f"- {genero['ID']}: {genero['Description']}")

def editar_genero():
    """Permite editar un género musical."""
    generos = cargar_datos(GENEROS_JSON)

    id_genero = input("Ingrese el ID del género a editar: ").strip()
    genero = next((g for g in generos if g["ID"] == id_genero), None)

    if not genero:
        print("❌ Género no encontrado.")
        return

    genero["Description"] = input(f"Nueva descripción ({genero['Description']}): ").strip() or genero["Description"]

    guardar_datos(GENEROS_JSON, generos)
    print("✅ Género editado correctamente.")

def eliminar_genero():
    """Elimina un género de la base de datos."""
    generos = cargar_datos(GENEROS_JSON)

    id_genero = input("Ingrese el ID del género a eliminar: ").strip()
    generos_filtrados = [g for g in generos if g["ID"] != id_genero]

    if len(generos) == len(generos_filtrados):
        print("❌ Género no encontrado.")
        return

    guardar_datos(GENEROS_JSON, generos_filtrados)
    print("✅ Género eliminado correctamente.")

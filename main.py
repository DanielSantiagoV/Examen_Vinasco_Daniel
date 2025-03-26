from modulos.artistas import agregar_artista, mostrar_artistas, editar_artista, eliminar_artista
from modulos.paises import agregar_pais, mostrar_paises, editar_pais, eliminar_pais
from modulos.generos import agregar_genero, mostrar_generos, editar_genero, eliminar_genero
from modulos.reportes import artistas_por_pais_y_tiempo, artistas_por_genero, artistas_ultimos_10_años

def mostrar_menu():
    """Muestra el menú principal con todas las opciones completas y permite salir correctamente."""
    while True:
        print("\n🎶 --- Menú Principal --- 🎶")
        print("1️⃣  Agregar Artista")
        print("2️⃣  Mostrar Artistas")
        print("3️⃣  Editar Artista")
        print("4️⃣  Eliminar Artista")
        print("5️⃣  Agregar País")
        print("6️⃣  Mostrar Países")
        print("7️⃣  Editar País")
        print("8️⃣  Eliminar País")
        print("9️⃣  Agregar Género")
        print("🔟  Mostrar Géneros")
        print("11️⃣ Editar Género")
        print("12️⃣ Eliminar Género")
        print("13️⃣ 📊 Reporte: Artistas Últimos 10 Años")
        print("14️⃣ 📊 Reporte: Artistas en Reino Unido (1960-1970)")
        print("15️⃣ 📊 Reporte: Artistas por Género 'Rock/pop'")
        print("16️⃣ ❌ Salir")

        opcion = input("Seleccione una opción: ").strip().lower()

        if opcion == "1":
            agregar_artista()
        elif opcion == "2":
            mostrar_artistas()
        elif opcion == "3":
            editar_artista()
        elif opcion == "4":
            eliminar_artista()
        elif opcion == "5":
            agregar_pais()
        elif opcion == "6":
            mostrar_paises()
        elif opcion == "7":
            editar_pais()
        elif opcion == "8":
            eliminar_pais()
        elif opcion == "9":
            agregar_genero()
        elif opcion == "10":
            mostrar_generos()
        elif opcion == "11":
            editar_genero()
        elif opcion == "12":
            eliminar_genero()
        elif opcion == "13":
            artistas_ultimos_10_años()
        elif opcion == "14":
            artistas_por_pais_y_tiempo("United Kingdom", 1960, 1970)
        elif opcion == "15":
            artistas_por_genero("Rock/pop")
        elif opcion in ["16", "salir", "exit", "❌"]:
            print("\n👋 Saliendo del sistema... ¡Hasta pronto! 🎵")
            break  # Sale del bucle y termina el programa
        else:
            print("⚠ Opción inválida, intente nuevamente.")

if __name__ == "__main__":
    mostrar_menu()

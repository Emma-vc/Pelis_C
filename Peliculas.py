from inicio import login,inicio_historial,acciones,registrar_accion, mostrar_historial,catalogo_flyer, menu_principal,eliminar_historial,HISTORIAL_TOTAL
from datetime import datetime
import os
BRIGHT_MAGENTA = "\x1B[95m"
RESET = "\x1B[0m"

#### POO + encapsulacion
##la clase pelicula tiene un atributo muy privado nombre
class Pelicula:
    def __init__(self, nombre=str):
        self.__nombre=nombre

    ## getter para leer el atributo nombre
    ## @property
    def get_nombre(self) -> str:
        return self.__nombre
    ## se puede acceder al atributo nombre muy privado y lo devuelve
    def __str__(self) -> str:
        return self.__nombre

## Se crea un constructor con atributo nombre y el de usuario valido que sirve para registras acciones
# la ruta se va a generar al poner el nombre de catalogo  
# ##los atributos de clase catalogoPeli son privados para que no se puedan usar en otra clase o en otro archivo py segun lo entendido
class catalogoPeliculas:
    def __init__(self, nombre_catalogo=str,usuario_valido=str):
        self._nombre=nombre_catalogo
        self._ruta_archivo=f"{nombre_catalogo}.txt"
        self._usuario_valido=usuario_valido
        self._iniciar_catalogo()

##Metodos getter para obtener nombre, ruta. iniciar catalogo comprueba su existencia          
    def get_nombre_catalogo(self) -> str:
        return self._nombre

    def get_ruta_archivo(self) -> str:
        return self._ruta_archivo
    ##creacion de catalogo en modo escritura w, si no existe lo crea
    def _iniciar_catalogo(self):
        if not os.path.exists(self._ruta_archivo):  # Solo crea si no existe
            try:
                with open(self._ruta_archivo, "w", encoding="utf-8") as archivo:
                    archivo.write("")  # Se crea un archivo vacio
                print(f"Creaste un nuevo catálogo: '{self._nombre}'")
                registrar_accion(self._usuario_valido,f"Creo un nuevo catalogo: '{self._nombre}'")
            except Exception as e:
                print(f"Error al crear el catálogo '{self._nombre}': {e}")
          

    ## metodo para la opcion 1 agregar con txt en modo a 
    def agregar_pelicula(self):
        while True:
            nombre_pelicula = input("Ingrese el nombre de la pelicula a agregar (o 'n' para volver al menú): ").strip()
            if nombre_pelicula.lower() == 'n':
                print("Regresando al menú principal.")
                break
            elif nombre_pelicula:
                movies = Pelicula(nombre_pelicula)
                try:
                    with open(self._ruta_archivo, "a", encoding="utf-8") as archivo:
                            archivo.write(f"{movies.get_nombre()} \n")
                    print("\n>>> Agregando película...\n")        
                    print(f"'{movies.get_nombre()}' se agregó al catálogo '{self._nombre}'.")
                    registrar_accion(self._usuario_valido,f"Agrego la pelicula: '{movies.get_nombre()}' al catalogo '{self._nombre}'")
                    break
                except Exception as e:
                 print(f"Error al agregar '{nombre_pelicula}': {e}")
            else:
                print("Debe ingresar un nombre de pelicula valido")  

    ## metodo para la opcion 2 listar peliculas enumeradas, lectura del txt en modo r read para leer todo y splitlines la divide en lineas
    def listar_peliculas(self):
        if not os.path.exists(self._ruta_archivo):
           print(f"El catálogo '{self._nombre}' no existe o no tiene películas")
           return

        try:
           with open(self._ruta_archivo, "r", encoding="utf-8") as archivo:
            movies = archivo.read().splitlines()

           if movies:
                print(f"\n--- PELICULAS EN EL CATALOGO '{self._nombre}' ---")
                for i, pelicula in enumerate(movies, start=1):
                    print(f"{i}. {pelicula}")
                    # print("-" * 30)
                registrar_accion(self._usuario_valido, f"Listo las peliculas del catalogo '{self._nombre}'")
           else:
                print(f"El catálogo '{self._nombre}' está vacío. No hay películas para mostrar")

        except Exception as e:
          print(f"Ocurrió un error al listar las películas: {e}")

    #### metodo para la opcion 3 eliminar catalogo
    def eliminar_catalogo(self)-> bool:
        if not os.path.exists(self._ruta_archivo):
            print(f"El catálogo '{self._nombre}' no existe o ya fue eliminado")
            return False   

        confirmacion = input(f"¿Estás seguro de que quieres eliminar el catálogo '{self._nombre}'? (s/n): ").lower().strip()
        
        if confirmacion == 's':
            try:
                os.remove(self._ruta_archivo)
                print(f"El catálogo '{self._nombre}' ha sido eliminado exitosamente")
                registrar_accion(self._usuario_valido,f"Elimino el catalogo: '{self._nombre}'")
                return True
            except Exception as e:
                print(f"Ocurrió un error al eliminar el catálogo: {e}")
                return False
        else:
            print("Operación de eliminación de catálogo cancelada")
            return False

""" Funcion principal, flujo de todo el programa catalogo🤞🏽"""

def main():
    usuario_valido = login() # a usuario lo busco en la funcion login para que salga del ambito local y se redefina en un ambito global 

    if usuario_valido:# la funcion inicio.. puede usar el usuario
        inicio_historial(usuario_valido)
        ## - Inicio de sesion
        registrar_accion(usuario_valido, "Reviso el catalogo")  

        ## - Muestra el flyer y pide el nombre de catalogo
        catalogo_flyer()
        while True:
            nombre_catalogo = input("Ingrese el nombre del catálogo de películas: ").strip()
            if nombre_catalogo:
                break
            print("El nombre del catálogo no puede estar vacío. Por favor, intente nuevamente 😊")
        catalogo_actual = catalogoPeliculas(nombre_catalogo, usuario_valido)     
       
    # bucle principal del menú de opciones
        while True:    
            opcion=menu_principal() 
            
            if opcion == 1:
                catalogo_actual.agregar_pelicula() 
                              
            elif opcion == 2:
                print(">>> Listando películas...")
                catalogo_actual.listar_peliculas() 
            elif opcion == 3:
                if catalogo_actual.eliminar_catalogo():
                    print("El catálogo actual ha sido eliminado. Saliendo del programa.....")
                    registrar_accion(usuario_valido, f"El usuario elimino un catalogo y cerro sesion a las {datetime.now().strftime('%H:%M')}")
                    break 
                # Opción 4 SALIR
            elif opcion == 4:
                print(">>> Saliendo del programa.... ¡Hasta luego!")
                registrar_accion(usuario_valido, f"Finalizo la sesion a las {datetime.now().strftime('%H:%M')}")
                break 
                                    
                # Opción 5 para ver el historial
            elif opcion == 5:
                    ###llamada a la funcion que muestra el historial
                mostrar_historial(usuario_valido)
                confirmar = input(f"\n¿Queres eliminar el historial {usuario_valido}? 🚮🗑️ (s/n): ").strip().lower()
                if confirmar == "s":
                 eliminar_historial(usuario_valido)
                 
    else:
        # si el usuario falla el login después de x intentos)
        print("\n 🚩 🚩 Error en el inicio de sesión 🚩 🚩 Saliendo de la aplicación....... ")

# para que el programa solo se ejecute en el archivo principal
if __name__ == "__main__":
    main()
# Inicia toda la aplicación    
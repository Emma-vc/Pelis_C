from inicio import login,inicio_historial,acciones,registrar_accion, mostrar_historial,catalogo_flyer, menu_principal,HISTORIAL_TOTAL
from datetime import datetime
import os

#### POO + encapsulacion
##la clase pelicula tiene un atributo muy privado nombre
class pelicula:
    def __init__(self, nombre=str):
        self.__nombre=nombre

    ## getter para leer el atributo nombre
    @property
    def nombre(self) -> str:
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
                registrar_accion(self._usuario_valido,f"Creó un nuevo catálogo: '{self._nombre}'")
            except Exception as e:
                print(f"Error al crear el catálogo '{self._nombre}': {e}")
                registrar_accion(self._usuario_valido, f"Error al crear el catálogo: '{self._nombre}' - {e}")
                
    def agregar_pelicula(self):
        pass
    def listar_peliculas(self):
        pass
    def eliminar_catalogo(self):
        pass


### funcion principal, que engloba a las del py inicio 
def app():
    usuario_valido = login() # a usuario lo busco en la funcion login para que salga del ambito local y se redefina en un ambito global creo

    if usuario_valido:
        # la funcion inicio.. puede usar el usuario
        inicio_historial(usuario_valido)
        # llamado a la funcion catalogo       
        

        # bucle principal del menú de opciones
        while True:
            catalogo_flyer()
            opcion=menu_principal() 
           
            if opcion == 1:
                print(">>> Agregando película...")
                # Llamar a la función para agregar película aquí
            elif opcion == 2:
                print(">>> Listando películas...")
                # Llamar a la función para listar películas aquí
            elif opcion == 3:
                print(">>> Eliminando catálogo...")
                # Llamar a la función para eliminar catálogo aquí
            elif opcion == 4:
                # Opción SALIR
                hora_salida = datetime.now().strftime("%H:%M")
                mensaje_salida = f"Finalizó la sesión a las {hora_salida}"
                
                # 'acciones' es la misma lista que importada. Añadir aquí.
                acciones.append(mensaje_salida)
                
                # 'usuario_valido' está definido y disponible en este punto
                with open(f"historial_{usuario_valido}.txt", "a") as archivo:
                    archivo.write(mensaje_salida + "\n")
                
                print(">>> Saliendo del programa. ¡Hasta luego!")
                break # Salir del bucle del menú
            elif opcion == 5:
                # Opción para ver el historial
                print("\n--- Historial de Sesión ---")
                if not acciones:
                    print("El historial de esta sesión está vacío.")
                else:
                    for accion in acciones:
                        print(accion)
                # print("---------------------------\n")
                RED_FG = "\x1B[31m"
                RESET = "\x1B[0m"
                print(f"{RED_FG}{'*'*50}{RESET}")
            else:
                print("Opción no válida. Por favor, intente de nuevo.")
    else:
        # Este 'else' solo se ejecutaría si tu función 'login()'
        # tuviera una forma de retornar `None` o `False` (por ejemplo,
        # si el usuario falla el login después de X intentos).
        print("\n 🚩 🚩 Error en el inicio de sesión 🚩 🚩 Saliendo de la aplicación....... ")

# para que el programa solo se ejecute en el archivo principal
if __name__ == "__main__":
    app()# Inicia toda la aplicación    
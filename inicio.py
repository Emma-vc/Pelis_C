from datetime import datetime
import os
HISTORIAL_TOTAL= "historial_general.txt"

## FUNCION Login estan contempladas las respectivas validaciones al ingreso, codigo ansi.  No crea un usuario, permite el ingreso de usuarios ya registrados

def login():
    personas = {"andrea": 6385, "nazarena": 8196, "roberta": 4221, "juan": 3697, "martin":2532}
    print("")
    CYAN = "\x1B[36m"
    RESET = "\x1B[0m"
    print(f"{CYAN}{'*'*11}{RESET} INICIAR SESION {CYAN}{'*'*11}{RESET}\n")
    
    max_intentos=3
    intentos_usuario=0
    usuario_valido = None

    ##Bucle 1 de validacion de ingreso para el usuario 
    while intentos_usuario < max_intentos:
        usuario = input("Ingrese su nombre de usuario: ").lower()
        if not usuario.isalpha():
            print("Solo puede ingresar letras --> 🅰️ 🅱️")
            continue
        
        if usuario not in personas:
            print("Usuario no registrado")
            intentos_usuario=intentos_usuario+1
            print(f"Quedan {max_intentos-intentos_usuario} intentos!!")
            if intentos_usuario==max_intentos:
                break # fin del limite de intentos 
            continue 
        ##usuario existente
        usuario_valido=usuario
        break
    ## Se terminaron los intentos para el usuario 
    if usuario_valido is None:
        RESET = "\x1B[0m"  
        ITALIC = "\x1B[3m"
        RED = "\x1B[31m" 
        print(f"\nLa cantidad de intentos máximos {max_intentos} fue superada por el usuario!!\n") 
        print(f"{RED}{ITALIC}  Acceso denegado!!!{RESET}")
        return None
    
    ### Bucle 2 de validacion de ingreso para la clave 
    intentos_clave=0   
    while intentos_clave < max_intentos:
        try:
            clave = int(input("Ingrese su contraseña: "))
            if clave==personas[usuario_valido]:
               GREEN = "\x1B[32m"
               RESET = "\x1B[0m"  
               ITALIC = "\x1B[3m"
               BOLD= "\x1B[1m"
               WHITE = "\x1B[37m"
               print(f"\n {GREEN}{ITALIC}Acceso permitido{RESET} \n")
               usuario_valido=usuario.capitalize()
               print(f" {BOLD}{WHITE}¡Hola! {usuario_valido}{RESET}")
               return usuario_valido
            else:
                 print("Contraseña incorrecta. Vuelva a intentar")
                 intentos_clave=intentos_clave+1
                 print(f"Quedan {max_intentos-intentos_clave} intentos!!")
        except ValueError:
                print("Por favor, ingrese solo números 1️⃣ 2️⃣ 3️⃣ ")
                intentos_clave=intentos_clave+1
                print(f"Quedan {max_intentos-intentos_clave} intentos!!")
                
    RESET = "\x1B[0m"  
    ITALIC = "\x1B[3m"
    RED = "\x1B[31m" 
    print(f"\n La cantidad de intentos maximos {max_intentos} fue superada!!\n") 
    print(f"{RED}{ITALIC}  Acceso denegado!!!{RESET}")           

### FUNCION de SEGUIMIENTO inciamos un seguimiento del usuario desde que ingresa, empezamos con el encabezado con su nombre y fecha y lo guardamos en el txt 
BRIGHT_MAGENTA = "\x1B[95m"
RESET = "\x1B[0m"
acciones=[]
def inicio_historial(usuario_valido):
    timestamp = datetime.now().strftime("%A %d-%m-%Y %H:%M")
    # separador = "-" * 80
    separador=(f"\n{BRIGHT_MAGENTA}{'*'*80}{RESET}")
    encabezado= f"{usuario_valido} ingreso el dia {timestamp}:"
    acciones.append(encabezado)
    with open(HISTORIAL_TOTAL,"a", encoding="utf-8") as archivo:
        archivo.write("\n" + separador + "\n")  #  línea de separación entre usuarios
        archivo.write("\n" + encabezado + "\n")

#Por cada usuario se va hacer un historial de lo que hizo desde que ingreso, si elimino agrego algo, se uso del enconding para evitar errores en el titulo de peliculas
def registrar_accion(usuario_valido, actividad):
    registro = f"- {actividad}"
    acciones.append(registro)
    with open(HISTORIAL_TOTAL, "a", encoding="utf-8") as archivo:
        archivo.write(registro + "\n")

##funcion mostrar historial de todos los usuarios, tambien registra esta actividad del usuario y tiene la opcion con una funcion anidada de borrar el historial
def mostrar_historial(usuario_valido):
    try:
        if not os.path.exists(HISTORIAL_TOTAL):
            print(f"El historial general aún está vacío. No hay acciones registradas")
            return

        with open(HISTORIAL_TOTAL, "r", encoding="utf-8") as archivo:
            historial_contenido = archivo.read().strip()
            
            if historial_contenido:
                print(f"\n--- Historial de Actividad ({HISTORIAL_TOTAL}) ---")
                print(historial_contenido)
                BRIGHT_MAGENTA = "\x1B[95m"
                RESET = "\x1B[0m"
                print(f"\n{BRIGHT_MAGENTA}{'*'*80}{RESET}")
            else:
                print(f"El historial general está vacío. No hay acciones registradas")
    except Exception as e:
        print(f"Ocurrió un error al mostrar el historial general: {e}")
      
 ###FUNCION eliminar historial

def eliminar_historial(usuario_valido):
    if os.path.exists(HISTORIAL_TOTAL):
        try:
            os.remove(HISTORIAL_TOTAL)
            print("Historial eliminado correctamente ✅")
            registrar_accion(usuario_valido, "Elimino el historial")
        except FileNotFoundError:
            print("No se encontró el archivo del historial")
    else:
        print("No hay historial para borrar")
             
###FUNCION INICIO CATALOGO
def catalogo_flyer():
      ITALIC = "\x1B[3m"
      BOLD = "\x1B[1m" 
      BRIGHT_CYAN_FG = "\x1B[96m"
      RESET = "\x1B[0m"
      print(f"\n {BRIGHT_CYAN_FG}{BOLD}{'⁓⁘'*8} C U E V A N A {ITALIC} New g {'⁓⁘'*8}{RESET}\n")
 

## FUNCION MENU
def menu_principal():
    
    opciones={ 1: "AGREGAR PELICULA 🎞️",
               2: "LISTAR PELICULAS 🧾",
               3: "ELIMINAR CATALOGO DE PELICULA 🗑️",
               4: "SALIR 🏃🏽‍♂️",
               5: "Ver historial registrado  🔍"}
    
    BRIGHT_MAGENTA = "\x1B[95m"
    BOLD = "\x1B[1m"
    RESET = "\x1B[0m"
    WHITE = "\x1B[37m"
    print(f"\n {BRIGHT_MAGENTA}{'⁘⁓'*5}{RESET}{BOLD}{WHITE} SELECCIONE UNA OPCION {RESET} {BRIGHT_MAGENTA}{'⁓⁘'*5}{RESET}\n")
   
    for numero,opcion in opciones.items():
        print(f"{numero}.{opcion}")

    while True:
        try:
            opcion = int(input("\n Que Desea hacer?: "))
            print("")
            if opcion in opciones:  # si la opción esta dentro de las disponibles la retorna
                return opcion
            else:
                print("Opción no válida 😖 Por favor, seleccione un número del menú")
        except ValueError:
            print("Entrada no válida 🚫 Por favor, ingrese un número")     

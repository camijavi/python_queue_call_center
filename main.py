# SISTEMA DE LLAMADAS DE DISNORTE-DISSUR:
# Un transformador explota en un barrio. De repente, 50 personas intenta llamar al centro 
# de atención al cliente al mismo tiempo para reportar que se quedaron sin energía y 
# tener un aproxiamdo de cuando será restaurado su servicio.

# Estructura seleccionada: Cola (Queue)

# Justificación: El centro de atención debe procesar las llamadas de forma equitativa, 
# bajo el principio FIFO (first in, first out). 
# El primer cliente que marcó y entró al sistema es el primero en ser atentido por un operador disponible.
# Nadie de los que llamo después puede saltarse la fila solo porque grití más fuerte.
# en llamdas telefonicas ellos ofrecen: consultas, reporte de averias y reclamo. 

# Se llama al 125, 134 o 135 (24/7)

# unico dato que se le solicita al cliente: Numero NISS

from queue import Llamada, ColaCallCenter
import os 

def main():
    cola = None
    opcion = 0
    
    while opcion != 8:
        print("******** Operaciones Sobre Cola (Call Center Disnorte-Dissur) ********")
        print("1. Crear Cola Vacia")
        print("2. Encolar Llamada (Registrar NISS)")
        print("3. Atender Siguiente Llamada (Desencolar)")
        print("4. Ver Siguiente Llamada en Espera (Visualizar Frente / Fondo)")
        print("5. Obtener Cantidad en Espera (Size)")
        print("6. Verificar si la Cola está Vacía (EstaVacio)")
        print("7. Vaciar Cola")
        print("8. Salir")
        print("**********************************************************************")
        try:
            opcion = int(input("SELECCIONE UNA OPCION: "))
        except ValueError:
            print("Entrada no válida. Por favor digite un número del 1 al 8.\n")
            continue
        
        match opcion:
            case 1:
                cola = ColaCallCenter()
                print("Cola vacia creada correctamente.\n")
            case 2:
                if cola is None:
                    print("La cola no ha sido creada. Debe crearla primero con la opción 1.\n")
                else:
                    niss = input("Digite el número NISS del cliente: ").strip()
                    if not niss:
                        print("Error: El número NISS no puede estar vacío.\n")
                    else:
                        llamada = Llamada(niss)
                        cola.encolarLlamada(llamada)
                        print(f"Llamada con NISS [{niss}] encolada exitosamente.\n")
            case 3:
                if cola is None:
                    print("La cola no ha sido creada. Debe crearla primero con la opción 1.\n")
                else:
                    llamada = cola.atenderSiguienteLlamada()
                    if llamada is None:
                        print("La cola esta vacia....!\n")
                    else:
                        print(f"Llamada atendida (Desencolada): [NISS: {llamada.niss} | Motivo: {llamada.motivo}]\n")
            case 4:
                if cola is None:
                    print("La cola no ha sido creada. Debe crearla primero con la opción 1.\n")
                else:
                    nodos = cola.peek_frente_fondo()
                    if nodos is None:
                        print("La cola esta vacia....!\n")
                    else:
                        frente, fondo = nodos
                        print(f"Frente (Siguiente llamada): [{frente.niss}] | Fondo (Última llamada): [{fondo.niss}]\n")
            case 5:
                if cola is None:
                    print("La cola no ha sido creada. Debe crearla primero con la opción 1.\n")
                else:
                    cantidad = cola.obtenerCantidadEnEspera()
                    print(f"Cantidad de clientes en espera: {cantidad}\n")
            case 6:
                if cola is None:
                    print("La cola no ha sido creada. Debe crearla primero con la opción 1.\n")
                else:
                    if cola.estaVacio():
                        print("La cola está vacía (No hay personas esperando en el conmutador).\n")
                    else:
                        print(f"La cola NO está vacía (Hay {cola.obtenerCantidadEnEspera()} persona(s) esperando en el conmutador).\n")
            case 7:
                if cola is None:
                    print("La cola no ha sido creada. Debe crearla primero con la opción 1.\n")
                else:
                    elementos = cola.vaciarCola()
                    if len(elementos) == 0:
                        print("La cola esta vacia....!\n")
                    else:
                        print("Cola vaciada exitosamente. Llamadas descartadas:")
                        for item in elementos:
                            item.print_llamada()
                        print()
            case 8:
                print("Saliendo del programa...\n")
            case _:
                print("Opción no válida. Por favor seleccione una opción entre 1 y 8.\n")

if __name__ == "__main__":
    main()

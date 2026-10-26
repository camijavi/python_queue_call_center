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
    conmutador = None
    opcion = 0
    
    while opcion != 8:
        print("******** Centro de Atención Telefónica - Disnorte-Dissur ********")
        print("1. Iniciar Conmutador de Llamadas")
        print("2. Registrar Llamada Entrante (Ingreso de NISS)")
        print("3. Atender Siguiente Llamada")
        print("4. Consultar Próxima Llamada en Espera")
        print("5. Consultar Total de Clientes en Espera")
        print("6. Verificar Estado del Conmutador")
        print("7. Finalizar Todas las Llamadas en Espera")
        print("8. Salir")
        print("*****************************************************************")
        try:
            opcion = int(input("SELECCIONE UNA OPCION: "))
        except ValueError:
            print("Entrada no válida. Por favor digite un número del 1 al 8.\n")
            continue
        
        match opcion:
            case 1:
                conmutador = ColaCallCenter()
                print("Conmutador de llamadas iniciado correctamente. Listo para recibir llamadas.\n")
            case 2:
                if conmutador is None:
                    print("El conmutador no ha sido iniciado. Debe iniciarlo primero con la opción 1.\n")
                else:
                    niss = input("Digite el número NISS del cliente: ").strip()
                    if not niss:
                        print("Error: El número NISS no puede estar vacío.\n")
                    else:
                        llamada = Llamada(niss)
                        conmutador.encolarLlamada(llamada)
                        print(f"Llamada con NISS [{niss}] registrada exitosamente en espera de atención.\n")
            case 3:
                if conmutador is None:
                    print("El conmutador no ha sido iniciado. Debe iniciarlo primero con la opción 1.\n")
                else:
                    llamada = conmutador.atenderSiguienteLlamada()
                    if llamada is None:
                        print("No hay llamadas en espera en este momento.\n")
                    else:
                        print(f"Llamada atendida: [NISS: {llamada.niss} | Motivo: {llamada.motivo}] - Asignada al operador.\n")
            case 4:
                if conmutador is None:
                    print("El conmutador no ha sido iniciado. Debe iniciarlo primero con la opción 1.\n")
                else:
                    nodos = conmutador.peek_frente_fondo()
                    if nodos is None:
                        print("No hay llamadas en espera en este momento.\n")
                    else:
                        primera, ultima = nodos
                        print(f"Siguiente llamada a ser atendida: [{primera.niss}] | Última llamada recibida: [{ultima.niss}]\n")
            case 5:
                if conmutador is None:
                    print("El conmutador no ha sido iniciado. Debe iniciarlo primero con la opción 1.\n")
                else:
                    cantidad = conmutador.obtenerCantidadEnEspera()
                    print(f"Cantidad de clientes en espera de atención: {cantidad}\n")
            case 6:
                if conmutador is None:
                    print("El conmutador no ha sido iniciado. Debe iniciarlo primero con la opción 1.\n")
                else:
                    if conmutador.estaVacio():
                        print("El conmutador está libre (No hay llamadas pendientes de atención).\n")
                    else:
                        print(f"El conmutador tiene llamadas pendientes (Hay {conmutador.obtenerCantidadEnEspera()} cliente(s) en espera).\n")
            case 7:
                if conmutador is None:
                    print("El conmutador no ha sido iniciado. Debe iniciarlo primero con la opción 1.\n")
                else:
                    elementos = conmutador.vaciarCola()
                    if len(elementos) == 0:
                        print("No hay llamadas en espera en este momento.\n")
                    else:
                        print("Se han finalizado todas las llamadas en espera. Llamadas despachadas:")
                        for item in elementos:
                            item.print_llamada()
                        print()
            case 8:
                print("Saliendo del sistema de atención...\n")
            case _:
                print("Opción no válida. Por favor seleccione una opción entre 1 y 8.\n")

if __name__ == "__main__":
    main()

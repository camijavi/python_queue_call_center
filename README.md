# Sistema de Llamadas Disnorte-Dissur (Cola / Queue)

Simulación interactiva de atención telefónica en un centro de atención al cliente (Call Center) para el reporte de averías de Disnorte-Dissur (125 / 134 / 135), implementada mediante una estructura de datos lineal tipo **Cola (Queue)** bajo el principio **FIFO** (*First In, First Out*).

## Caso de Uso
Un transformador explota en un barrio. De repente, 50 personas intentan llamar al centro de atención al cliente al mismo tiempo para reportar que se quedaron sin energía y tener un aproximado de cuándo será restaurado su servicio.

El conmutador debe procesar las llamadas de forma equitativa: el primer cliente en marcar es el primero en ser atendido por un operador disponible.

- **Estructura:** Cola enlazada (`ColaCallCenter`)
- **Nodo:** Llamada (`Llamada`)
- **Dato solicitado:** Número NISS (Número de Identificación de Suministro)

## Operaciones Disponibles
1. **Crear Cola Vacia**: Inicializa el conmutador.
2. **Encolar Llamada (Enqueue)**: Registra una nueva llamada al final de la fila mediante su NISS.
3. **Atender Siguiente Llamada (Dequeue)**: Desencola al primer cliente en espera para ser atendido por el operador.
4. **Ver Siguiente Llamada en Espera (Peek)**: Consulta el cliente al frente de la cola y el último en el fondo.
5. **Obtener Cantidad en Espera (Size)**: Conteo en tiempo real de clientes en espera.
6. **Verificar si la Cola está Vacía (EstaVacio / IsEmpty)**: Valida si el conmutador está libre o tiene llamadas.
7. **Vaciar Cola**: Despacha/cancela todas las llamadas restantes en espera.
8. **Salir**

## Ejecución
```bash
python3 main.py
```

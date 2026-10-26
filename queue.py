# Definición de las estructuras de datos
class Llamada:
    def __init__(self, niss: str, motivo: str = "Reporte de avería"):
        self.niss = str(niss)
        self.motivo = motivo
        self.data = self.niss  # Compatibilidad con Node.data
        self.next = None

    def print_llamada(self):
        print(f"[NISS: {self.niss} | Motivo: {self.motivo}]")

    def print_node(self):
        self.print_llamada()

    def __str__(self):
        return f"[NISS: {self.niss} | Motivo: {self.motivo}]"


class ColaCallCenter:
    def __init__(self):
        self.front = None
        self.back = None

    def estaVacio(self) -> bool:
        return self.front is None

    def isEmpty(self) -> bool:
        return self.estaVacio()

    def EstaVacio(self) -> bool:
        return self.estaVacio()

    def encolarLlamada(self, nueva: Llamada):
        if not isinstance(nueva, Llamada):
            nueva = Llamada(str(nueva))
        if self.front is None:
            self.front = nueva
            self.back = nueva
        else:
            self.back.next = nueva
            self.back = nueva

    def EncolarLlamada(self, nueva: Llamada):
        self.encolarLlamada(nueva)

    def enqueue(self, nueva: Llamada):
        self.encolarLlamada(nueva)

    def atenderSiguienteLlamada(self) -> Llamada:
        if self.front is None:
            return None
        else:
            llamada = Llamada(self.front.niss, self.front.motivo)
            if self.front.next is not None:
                self.front = self.front.next
            else:
                self.front = None
                self.back = None
            return llamada

    def AtenderSiguienteLlamada(self) -> Llamada:
        return self.atenderSiguienteLlamada()

    def dequeue(self) -> Llamada:
        return self.atenderSiguienteLlamada()

    def verSiguienteLlamada(self) -> Llamada:
        if self.front is None:
            return None
        return Llamada(self.front.niss, self.front.motivo)

    def VerSiguienteLlamada(self) -> Llamada:
        return self.verSiguienteLlamada()

    def peek(self) -> Llamada:
        return self.verSiguienteLlamada()

    def peek_frente_fondo(self) -> tuple[Llamada, Llamada]:
        if self.front is None:
            return None
        return Llamada(self.front.niss, self.front.motivo), Llamada(self.back.niss, self.back.motivo)

    def obtenerCantidadEnEspera(self) -> int:
        contador = 0
        actual = self.front
        while actual is not None:
            contador += 1
            actual = actual.next
        return contador

    def ObtenerCantidadEnEspera(self) -> int:
        return self.obtenerCantidadEnEspera()

    def size(self) -> int:
        return self.obtenerCantidadEnEspera()

    def clear(self) -> list[Llamada]:
        lista = []
        while self.front is not None:
            n = self.atenderSiguienteLlamada()
            lista.append(n)
        return lista

    def vaciarCola(self) -> list[Llamada]:
        return self.clear()

    def VaciarCola(self) -> list[Llamada]:
        return self.clear()


# Aliases para mantener compatibilidad con python_queue
Node = Llamada
Cola = ColaCallCenter
Queue = ColaCallCenter

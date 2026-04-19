class Nodo:

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:

    def __init__(self):
        self.cabeza = None
        self.size = 0

    def agregar(self, dato):
        newNode = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = newNode
        else:
            current = self.cabeza
            while current.siguiente is not None:
                current = current.siguiente
            current.siguiente = newNode

        self.size += 1

    def resumenTransacciones(self):
        resumen = []
        current = self.cabeza
        while current is not None:
            resumen.append(current.dato)
            current = current.siguiente
        return resumen
    
    
    def __len__(self):
        return self.size
    

    def __str__(self):
        elementos = self.resumenTransacciones()
        if not elementos:
            return "No hay transacciones registradas."
        return "\n".join(str(e) for e in elementos)
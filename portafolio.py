from historial import ListaEnlazada
from activos import 
from transacciones import 
from datetime import date

class Portafolio:

    def __init__(self,capitalInicial:float):
        self.capitalDisponible = capitalInicial
        self.acciones = dict[str, """Acciones"""] = {}
        
        

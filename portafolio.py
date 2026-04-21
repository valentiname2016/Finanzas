from historial import ListaEnlazada
from acciones import Acciones
#from transacciones import 
from datetime import date

class Portafolio:

    def __init__(self,capitalInicial:float):
        self.capitalDisponible = capitalInicial
        self.acciones = dict[str, Acciones] = {}
        #self.cdt/bonos
        self.historialTransacciones = ListaEnlazada()
        self.historialValor: list[tuple] = []
        self.diaActual = 0

        print(f"Portafolio creado con capital inicial de: {self.capitalDisponible}")

    
    def comprar(self, ticker:str, cantidad:int, fechaCompra:date=None) -> bool:
        
        if ticker not in self.acciones:
            print(f"El ticker {ticker} no se encuentra registrado en el portafolio. ")
            return False

        accion = self.acciones[ticker]
        fecha  = fechaCompra or date.today()

        print(f"  Verificando precio de {ticker} para el {fecha}...")
        precio = accion.obtenerDatos(fecha)

        if precio == 0:
            print(f"No se puede obtener el precio de {ticker} "
                  f"para la fecha {fecha}.")
            return False

        
        
    
    def vender(self, ticker:str, cantidad:int, fechaVenta:date=None) -> bool:
        
        if ticker not in self.acciones:
            print(f"El ticker {ticker} no se encuentra registrado en el portafolio.")
            return False
        
        accion = self.acciones[ticker]
        fecha  = fechaVenta or date.today()

        print(f"  Verificando precio de {ticker} para el {fecha}...")
        precio = accion.precioDeFecha(fecha)

        if precio == 0:
            print(f"No se pudo obtener el precio de {ticker} "
                  f"para la fecha {fecha}.")
            return False
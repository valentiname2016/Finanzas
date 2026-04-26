from historial import ListaEnlazada
from acciones import Acciones
from transacciones import Transaccion
from CDTBonos import CDTBonos

from datetime import timedelta, date
import matplotlib.pyplot as plt


class Portafolio:

    def __init__(self, capital_inicial):
        self.capital_inicial = capital_inicial
        self.capital_disponible = capital_inicial
        self.historial = ListaEnlazada()
        self.posiciones = {}
        self.valores_totales = []
        self.ganancia_por_dividendos = 0.0
        self.mi_cdt = None

    
    def agregar_accion(self, ticker):
        if ticker not in self.posiciones:
            self.posiciones[ticker] = 0
            print(f"Acción {ticker} agregada.")



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
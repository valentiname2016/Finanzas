from acciones import Acciones
from transacciones import Transaccion
from CDTBonos import CDTBonos
from historial import ListaEnlazada
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

    def comprar(self, ticker, cantidad, fecha):
        obj_accion = Acciones(ticker)
        datos = obj_accion.obtener_datos_dia(fecha)

        if datos != None:
            precio = datos["close"]
            costo_total = precio * cantidad

            if self.capital_disponible >= costo_total:
                self.capital_disponible = self.capital_disponible - costo_total
                self.posiciones[ticker] = self.posiciones[ticker] + cantidad
                
                nueva_t = Transaccion("COMPRA", ticker, cantidad, precio, fecha)
                self.historial.agregar(nueva_t)
                print("Compra exitosa.")
            else:
                print("No tienes suficiente dinero.")
        else:
            print("No se encontraron precios para esa fecha.")

    def agregar_cdt(self, tasa, plazo, monto):
        if self.capital_disponible >= monto:
            self.mi_cdt = CDTBonos(tasa, plazo, monto)
            self.capital_disponible = self.capital_disponible - monto
            print("CDT creado.")
        else:
            print("No tienes dinero suficiente para el CDT.")

    def simular(self, fecha_inicio, fecha_fin):
        self.valores_totales = []
        self.ganancia_por_dividendos = 0.0
        fecha_actual = fecha_inicio

        while fecha_actual <= fecha_fin:
            valor_acciones_hoy = 0.0
            
            for ticker in self.posiciones:
                cantidad = self.posiciones[ticker]
                if cantidad > 0:
                    obj = Acciones(ticker)
                    datos = obj.obtener_datos_dia(fecha_actual)
                    
                    if datos != None:
                        precio = datos["close"]
                        valor_acciones_hoy = valor_acciones_hoy + (precio * cantidad)
                        
                        if datos["dividendo"] > 0:
                            pago = datos["dividendo"] * cantidad
                            self.capital_disponible = self.capital_disponible + pago
                            self.ganancia_por_dividendos = self.ganancia_por_dividendos + pago

            valor_cdt_hoy = 0.0
            if self.mi_cdt != None:
                self.mi_cdt.aplicarInteresDiario()
                valor_cdt_hoy = self.mi_cdt.valorTotal()

            total_dia = self.capital_disponible + valor_acciones_hoy + valor_cdt_hoy
            self.valores_totales.append(total_dia)

            fecha_actual = fecha_actual + timedelta(days=1)

    def resumen(self):
        if len(self.valores_totales) > 0:
            valor_final = self.valores_totales[-1]
            rentabilidad = (valor_final - self.capital_inicial) / self.capital_inicial
            
            print("\nRESUMEN")
            print(f"Capital Inicial: {self.capital_inicial:.2f}")
            print(f"Valor Final: {valor_final:.2f}")
            print(f"Rentabilidad Total: {rentabilidad:.2%}")
            print(f"Ganancia solo por Dividendos: {self.ganancia_por_dividendos:.2f}")
            
            if self.mi_cdt != None:
                print(f"Ganancia solo por CDT: {self.mi_cdt.interes_acumulado:.2f}%")
        else:
            print("Primero debes correr la simulación.")

    def grafica(self):
        if len(self.valores_totales) > 0:
            plt.plot(self.valores_totales)
            plt.title("Evolución del Portafolio")
            plt.savefig('grafica_portafolio.png')
            print("Gráfica guardada.")
import yfinance as yf

class Acciones:
    def __init__(self, ticker):
        self.ticker=ticker
        self.precioInicial=0.0
        self.precioMinimo=0.0
        self.precioMaximo=0.0
        self.precioCierre=0.0
        self.dividendo=0.0

    def obtenerDatos(self):
        data=yf.download(self.ticker, period="1d")
        
        if not data.empty:
            self.precioInicial=float(data['Open'].iloc[-1])
            self.precioMinimo=float(data['Low'].iloc[-1])
            self.precioMaximo=float(data['High'].iloc[-1])
            self.precioCierre=float(data['Close'].iloc[-1])

            if 'Dividends' in data.columns:
                self.dividendo=float(data['Dividends'].iloc[-1])
            else:
                self.dividendo=0.0
        else:
            print("No se pudieron obtener datos")

    def rentabilidad(self):
        if self.precioMinimo != 0:
            return (self.precioCierre-self.precioInicial)-self.precioInicial
        else:
            return 0
        
    def mostrarDatos(self):
        print(f"Acción: {self.ticker}")
        print(f"Precio inicial: {self.precioInicial}")
        print(f"Precio mínimo: {self.precioMinimo}")
        print(f"Precio máximo: {self.precioMaximo}")
        print(f"Precio cierre: {self.precioCierre}")
        print(f"Dividendo: {self.dividendo}")
        #print(f"Rentabilidad: {self.rentabilidad():.2%}")


        

        
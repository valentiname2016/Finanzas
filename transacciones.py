class Transaccion:
    def __init__(self, tipo, ticker, cantidad, precio, fecha):
        self.tipo = tipo
        self.ticker = ticker
        self.cantidad = cantidad
        self.precio = precio
        self.fecha = fecha
 
    def __str__(self):
        return f"{self.fecha} | {self.tipo} | {self.ticker} | Cantidad: {self.cantidad} | Precio: {self.precio}"
class transacciones:
    def __init__(self, tipo , ticker, cantidad, precio, comision):
        self.tipo = tipo
        self.ticker = ticker
        self.cantidad = cantidad
        self.precio = precio
        self.comision = comision
    def costoTotal(self): 
        total= self.cantidad*self.precio
        if self.tipo=="compra":
            total= total + self.comision
        else:
            total= total-self.comision
        return total
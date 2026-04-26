class CDTBonos:
    def __init__(self, tasa, plazo, capital_invertido):
        self.tasa = float(tasa)
        self.plazo = int(plazo)
        self.capital_invertido = float(capital_invertido)
        self.interes_acumulado = 0.0
 
    def aplicarInteresDiario(self):
        interes_del_dia = (self.tasa / 365) * self.capital_invertido
        self.interes_acumulado = self.interes_acumulado + interes_del_dia
 
    def valorTotal(self):
        return self.capital_invertido + self.interes_acumulado
     
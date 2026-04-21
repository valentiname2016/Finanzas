class CDTBonos:
    def __init__(self, tasa, plazo, capitalinvertido, interesAcumulado):
        self.tasa =float(tasa)
        self.plazo =int(plazo)
        self.capitalinvertido =float (capitalinvertido)
        self.interesAcumulado = float(interesAcumulado)
    def AplicarinteresDiario(self):
        interes_diario = (self.tasa / 365) * self.capitalinvertido
        self.interesAcumulado += interes_diario

    def valorTotal(self):
        return self.capitalinvertido + self.interesAcumulado
     
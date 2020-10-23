from unittest import result
from unicodedata import decimal


class Finanzas:
    def __init__(
        self,
    ):
        self.cuenta = 0.00

    def cuentaFinal(self):
        self.cuenta = result
        return result


class ingresos:
    def __init__(self, ingresos):
        Finanzas.__init__(self)
        self.ingresos = ingresos

    def addIngreso(self):
        self.cuenta = self.cuenta + self.ingresos
        return self.cuenta


class egreso:
    def __init__(self, egreso):
        Finanzas.__init__(self)
        self.egreso = egreso
        
    def addEgreso(self):
        self.cuenta = self.cuenta - self.egreso
        return self.cuenta


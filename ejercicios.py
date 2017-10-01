"""
    Autor: Diego Misael Blanco Murillo y Cruz Eduardo Lopez Sandoval
    Fecha: 21/SEP/17
"""


class Ejercicios():

    def __init__(self):
        self.resultado = 0
        self.noNumerosCeros = 'No se aceptan numeros menores o iguales a cero'

    def obtener_resultado(self):
        return self.resultado

    def comision_ventas(self, sueldo, venta1, venta2, venta3):
        try:
            if (type(sueldo) == str or type(venta1) == str
                    or type(venta2) == str or type(venta3) == str):
                self.resultado = 'Datos incorrectos'
            elif (sueldo <= 0 or venta1 <= 0 or venta2 <= 0
                  or venta3 <= 0):
                self.resultado = self.noNumerosCeros
            else:
                self.comision = venta1 * 0.10
                self.comision += venta2 * 0.10
                self.comision += venta3 * 0.10
                self.resultado = sueldo + self.comision
        except:
            self.resultado = "Datos incorrectos"

    def descuento_compra(self, num1):
        try:
            if type(num1) == str:
                self.resultado = 'Datos incorrectos'
            elif num1 <= 0:
                self.resultado = self.noNumerosCeros
            else:
                self.descuento = num1 * 0.15
                self.resultado = num1 - self.descuento
        except:
            self.resultado = "Datos incorrectos"

    def calificacion_final(self, parcialUno, parcialDos, parcialTres):
        try:
            if (type(parcialUno) == str or type(parcialDos) == str
                    or type(parcialTres) == str):
                self.resultado = 'Datos incorrectos'
            else:
                self.resultado = (parcialUno + parcialDos + parcialTres) / 3
        except:
            self.resultado = "Datos incorrectos"

    def porcentaje_hombres_mujeres(self, numHombres, numMujeres):
        try:
            if type(numHombres) == str or type(numMujeres) == str:
                self.resultado = 'Datos incorrectos'
            elif numHombres <= 0 or numMujeres <= 0:
                self.resultado = self.noNumerosCeros
            else:
                self.total = numHombres + numMujeres
                self.porcentajeHombres = numHombres * 100 / self.total
                self.porcentajeMujeres = numMujeres * 100 / self.total
                self.porcentaje = [
                    self.porcentajeHombres, self.porcentajeMujeres]
                self.resultado = self.porcentaje
        except:
            self.resultado = "Datos incorrectos"

    def dolar_a_pesos_mx(self, dolar, pesos):
        try:
            if type(dolar) == str or type(pesos) == str:
                self.resultado = 'Datos incorrectos'
            elif dolar <= 0 or pesos <= 0:
                self.resultado = self.noNumerosCeros
            else:
                self.resultado = dolar * pesos
        except:
            self.resultado = "Datos incorrectos"

    def salario_obrero(self, salario, salarioAnterior):
        try:
            self.resultado = salario + salarioAnterior * 0.25
        except:
            self.resultado = "Datos incorrectos"

    def area_circulo(self, radio):
        try:
            self.radio = self.numValidator(radio)
            self.resultado = 3.1416 * (radio**2)
        except:
            self.resultado = "Datos incorrectos"

    def metros_pies_pulgadas(self, metros):
        try:
            self.medidas = list()
            self.metrosCM = metros * 100
            self.pulgadas = self.metrosCM / 2.54
            self.pies = self.metrosCM / 30.48
            self.medidas.insert(0, self.pulgadas)
            self.medidas.insert(1, self.pies)

            return self.medidas
        except:
            self.resultado = "Datos incorrectos"

    def elevar_al_cubo(self, numero):
        self.resultado = numero ** 3

    def kilos_a_gr_lb_tons(self, kilos):
        try:
            self.unidadeaPeso = list()
            self.kgGr = kilos * 1000
            self.kgLib = kilos * 2.20461999989109
            self.kgTons = kilos * 0.001
            self.unidadeaPeso.insert(0, self.kgGr)
            self.unidadeaPeso.insert(1, self.kgLib)
            self.unidadeaPeso.insert(2, self.kgTons)

            return self.unidadeaPeso
        except:
            return "Datos incorrectos"

    def numValidator(self, num):
        return int(num)

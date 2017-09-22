import math

"""
    Autor: Diego Misael Blanco Murillo.
    Fecha: 06/SEP/17
"""


class Ejercicios():

    def __init__(self):
        self.resultado = 0

    def obtener_resultado(self):
        return self.resultado

    def comision_ventas(self, sueldo, venta1, venta2, venta3):
        try:
            self.comision = venta1 * 0.10
            self.comision += venta2 * 0.10
            self.comision += venta3 * 0.10
            self.resultado = sueldo + self.comision
        except:
            self.resultado = 'Datos incorrectos'

    def descuento_compra(self, num1):
        try:
            self.descuento = num1 * 0.15
            self.resultado = num1 - self.descuento
        except:
            self.resultado = 'Datos incorrectos'

    def porcentaje_hombres_mujeres(self, numHombres, numMujeres):
        try:
            self.total = numHombres + numMujeres
            self.porcentajeHombres = numHombres / self.total * 100
            self.porcentajeMujeres = numMujeres / self.total * 100
            self.porcentaje = [self.porcentajeHombres, self.porcentajeMujeres]
            self.resultado = self.porcentaje

        except:
            self.resultado = 'Datos incorrectos'
    def dolar_a_pesos_mx(self, dolar, pesos):
        try:
            self.resultado = dolar * pesos
        except:
            self.resultado = 'Datos incorrectos'

    def salario_obrero(self, salario, salarioAnterior):
        try:
            self.resultado = salario + salarioAnterior * 0.25
        except:
            self.resultado = 'Datos incorrectos'

    def area_circulo(self, radio):
        try:
            self.resultado = 3.1416 * (radio**2)
        except:
            self.resultado = 'Datos incorrectos'

    def metros_pies_pulgadas(self, metros):
        try:
            self.medidas = list()
            self.metrosCM = metros*100
            self.pulgadas = metrosCM/2.54
            self.pies = metrosCM/30.48
            self.medidas.append(self.pulgadas)
            self.medidas.append(self.pies)

            self.resultado = self.medidas
        except:
            self.resultado = 'Datos incorrectos'

    def elevar_al_cubo(self, numero):
        self.resultado = numero ** 3   

    def kilos_a_gr_lb_tons(kilos):
                        
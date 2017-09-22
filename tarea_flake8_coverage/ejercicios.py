import math


class Ejercicios():

    def __init__(self):
        self.resultado = 0
        self.metrosCM = 0.0

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
            self.radio = self.numValidator(radio)
            self.resultado = 3.1416 * (radio**2)
        except ValueError as valEr:
            self.resultado = 'Datos incorrectos'

    def metros_pies_pulgadas(self, metros):
        try:
            self.medidas = list()
            self.metrosCM = metros*100
            self.pulgadas = self.metrosCM/2.54
            self.pies = self.metrosCM/30.48
            self.medidas.insert(0,self.pulgadas)
            self.medidas.insert(1,self.pies)

            return self.medidas
        except:
            return "Datos incorrectos"   

    def elevar_al_cubo(self, numero):
        self.resultado = numero ** 3   

    def kilos_a_gr_lb_tons(self, kilos):
        try:
            self.unidadeaPeso = list()
            self.kgGr = kilos * 1000
            self.kgLib = kilos * 2.20461999989109
            self.kgTons = kilos * 0.001
            self.unidadeaPeso.insert(0,self.kgGr)
            self.unidadeaPeso.insert(1,self.kgLib)
            self.unidadeaPeso.insert(2,self.kgTons)

            return self.unidadeaPeso
        except:
             return "Datos incorrectos"           
                        
    def numValidator(self,num):
        return int(num)                    
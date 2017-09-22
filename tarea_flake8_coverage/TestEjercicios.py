import unittest
from ejercicios import Ejercicios
"""
	Autor: Diego Misael Blanco Murillo y Cruz Eduardo Lopez Sandoval
	Fecha: 21/SEP/17
"""
class CalculadoraTest(unittest.TestCase):
	
	def setUp(self):
		self.ejer = Ejercicios()
		self.datosIncorrectos = 'Datos incorrectos'
	
	def test_comision_ventas(self):
		self.ejer.comision_ventas(100, 300, 400, 800)
		self.assertEquals(self.ejer.obtener_resultado(), 250)
	
	def test_descuento_15_porciento(self):
		self.ejer.descuento_compra(100)
		self.assertEquals(self.ejer.obtener_resultado(), 85)
	
	"""def test_porcentaje_hombres_mujeres(self):
		self.ejer.porcentaje_hombres_mujeres(14, 7)
		self.assertEquals(self.ejer.obtener_resultado(), [66.66, 33.33])"""
	
	def test_dolar_a_pesos_mx(self):
		self.ejer.dolar_a_pesos_mx(17.832623, 18)
		self.assertEquals(self.ejer.obtener_resultado(), 320.98721400000005)

	def test_salario_obrero(self):
		self.ejer.salario_obrero(200,160)	
		self.assertEquals(self.ejer.obtener_resultado(), 240)
			
	def test_area_circulo(self):
		self.ejer.area_circulo(6)
		self.assertEquals(self.ejer.obtener_resultado(), 113.0976)

	"""def test_metros_a_pies_y_pulgadas(self):
		self.ejer.metros_pies_pulgadas(5)
		self.assertEquals(self.ejer.obtener_resultado(),[196.850393701,16.404199475])"""

	def test_elevar_al_cubo_un_numero(self):
		self.ejer.elevar_al_cubo(3)
		self.assertEquals(self.ejer.obtener_resultado(), 27)	

	def test_peso_a_gramos_libras_tons(self):
		self.ejer.kilos_a_gr_lb_tons(70)	
		self.assertEquals(sel.ejer.obtener_resultado(),)

	def tearDown(self):
		pass

if __name__ == '__main__':
	unittest.main()
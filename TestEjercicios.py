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
		self.noAceptanCeros = 'No se aceptan numeros menores o iguales a cero'
	
	def test_comision_ventas(self):
		self.ejer.comision_ventas(100, 300, 400, 800)
		self.assertEquals(self.ejer.obtener_resultado(), 250)

	def test_comision_ventas_no_acepta_letras(self):
		self.ejer.comision_ventas('m', 'z', 'b', 'v')
		self.assertEquals(self.ejer.obtener_resultado(), self.datosIncorrectos)

	def test_comision_ventas_no_acepta_numeros_menores_a_cero(self):
		self.ejer.comision_ventas(0, 0, 0, 0)
		self.assertEquals(self.ejer.obtener_resultado(), self.noAceptanCeros)		
	
	def test_descuento_15_porciento(self):
		self.ejer.descuento_compra(100)
		self.assertEquals(self.ejer.obtener_resultado(), 85)

	def test_descuento_15_porciento_no_acepta_letras(self):
		self.ejer.descuento_compra('x')
		self.assertEquals(self.ejer.obtener_resultado(), self.datosIncorrectos)
	
	def test_descuento_15_porciento_no_acepta_numeros_menores_a_cero(self):
		self.ejer.descuento_compra(-99)
		self.assertEquals(self.ejer.obtener_resultado(), self.noAceptanCeros)

	def test_calificacion_final(self):
		self.ejer.calificacion_final(10, 9, 8)
		self.assertEquals(self.ejer.obtener_resultado(), 9)

	def test_calificacion_final_no_acepta_letras(self):
		self.ejer.calificacion_final('V', 9, 8)
		self.assertEquals(self.ejer.obtener_resultado(), self.datosIncorrectos)

	def test_calificacion_final_numeros_float_igual_a_9_166666667(self):
		self.ejer.calificacion_final(10, 9.5, 3.5)
		self.assertEquals(self.ejer.obtener_resultado(), 7.666666666666667)

	def test_porcentaje_hombres_mujeres(self):
		self.ejer.porcentaje_hombres_mujeres(14, 7)
		self.assertEquals(self.ejer.obtener_resultado(), [66, 33])

	def test_porcentaje_hombres_mujeres_no_acepta_letras(self):
		self.ejer.porcentaje_hombres_mujeres('v', 7)
		self.assertEquals(self.ejer.obtener_resultado(), self.datosIncorrectos)

	def test_porcentaje_hombres_mujeres_no_acepta_numeros_menores_a_cero(self):
		self.ejer.porcentaje_hombres_mujeres(0, -7)
		self.assertEquals(self.ejer.obtener_resultado(), self.noAceptanCeros)
	
	def test_dolar_a_pesos_mx(self):
		self.ejer.dolar_a_pesos_mx(17.832623, 18)
		self.assertEquals(self.ejer.obtener_resultado(), 320.98721400000005)

	def test_dolar_a_pesos_mx_no_acepta_letras(self):
		self.ejer.dolar_a_pesos_mx('M', 19)
		self.assertEquals(self.ejer.obtener_resultado(), self.datosIncorrectos)

	def test_dolar_a_pesos_mx_no_acepta_numeros_menores_a_cero(self):
		self.ejer.dolar_a_pesos_mx(0, -1)
		self.assertEquals(self.ejer.obtener_resultado(), self.noAceptanCeros)

	def test_salario_obrero(self):
		self.ejer.salario_obrero(200,160)	
		self.assertEquals(self.ejer.obtener_resultado(), 240)

	def test_salario_obrero_negativos(self):
		self.ejer.salario_obrero(-200,-160)	
		self.assertEquals(self.ejer.obtener_resultado(), -240)

	def test_salario_obrero_sin_porcentaje(self):
		self.ejer.salario_obrero(200,0)	
		self.assertEquals(self.ejer.obtener_resultado(), 200)		
			
	def test_area_circulo_radio_int(self):
		self.ejer.area_circulo(6)
		self.assertEquals(self.ejer.obtener_resultado(), 113.0976)

	def test_area_circulo_radio_float(self):
		self.ejer.area_circulo(6.5)
		self.assertEquals(self.ejer.obtener_resultado(), 132.7326)
		
	def test_area_circulo_radio_negativo(self):
		self.ejer.area_circulo(-6)
		self.assertEquals(self.ejer.obtener_resultado(), 113.0976)		
		
	def test_metros_a_pies_y_pulgadas_un_metro(self):
		self.assertEquals(self.ejer.metros_pies_pulgadas(1),[39.37007874015748, 3.2808398950131235])

	def test_metros_a_pies_y_pulgadas_numero_negativo(self):
		self.assertEquals(self.ejer.metros_pies_pulgadas(-1),[-39.37007874015748, -3.2808398950131235])
		
	def test_metros_a_pies_y_pulgadas(self):
		self.assertEquals(self.ejer.metros_pies_pulgadas(5),[196.8503937007874,16.404199475065617])		

	def test_elevar_al_cubo_un_numero(self):
		self.ejer.elevar_al_cubo(3)
		self.assertEquals(self.ejer.obtener_resultado(), 27)

	def test_elevar_al_cubo_un_numero_negativo(self):
		self.ejer.elevar_al_cubo(-1)
		self.assertEquals(self.ejer.obtener_resultado(), -1)

	def test_elevar_al_cubo_cero(self):
		self.ejer.elevar_al_cubo(0)
		self.assertEquals(self.ejer.obtener_resultado(), 0)			

	def test_peso_a_gramos_libras_tons(self):	
		self.assertEquals(self.ejer.kilos_a_gr_lb_tons(70),[70000,154.3233999923763,0.07])

	def test_peso_a_gramos_libras_tons_kg_cero(self):	
		self.assertEquals(self.ejer.kilos_a_gr_lb_tons(0),[0,0.0,0.0])

	def test_peso_a_gramos_libras_tons_kg_letras(self):	
		self.assertEquals(self.ejer.kilos_a_gr_lb_tons("KIlos"), "Datos incorrectos")	
	
	def tearDown(self):
		pass

if __name__ == '__main__': # pragma: no cover
	unittest.main()
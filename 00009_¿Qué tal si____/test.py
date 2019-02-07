class TestFixtures(unittest.TestCase):
  
  def test_dia_de_semana(self):
    self.assertTrue(dia_de_semana in globals(), 'La variable dia_de_semana no existe')
    self.assertTrue(dia_de_semana == 'domingo', 'El valor de dia de semana es incorrecto.')
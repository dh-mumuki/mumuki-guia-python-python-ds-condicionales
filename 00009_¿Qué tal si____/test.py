class TestFixtures(unittest.TestCase):
  
  def test_dia_de_semana(self):
    self.assertTrue(actividad.lower() == 'domingo', 'El valor de dia de semana es incorrecto.')
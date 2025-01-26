# test_cities.py
import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):

    def test_city_country(self):
        """This test verifies the city_country function."""
        formatted_string = city_country('santiago', 'chile')
        self.assertEqual(formatted_string, 'Santiago, Chile')
        
            
if __name__ == '__main__':
    unittest.main()    
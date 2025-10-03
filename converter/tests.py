#converter/tests.py
import unittest

from pkg.conversions import _convert_units_temp


class TestConversionResults(unittest.TestCase):
    def setUp(self):
        self.convert = _convert_units_temp
 
    # Temperature test cases
    def test_fahrenheit_to_celsius(self):
        result = self.convert(212, "fahrenheit", "celsius")
        self.assertAlmostEqual(result, 100.0, places = 2)

    def test_celsius_to_fahrenheit(self):
        result = self.convert(32, "celsius", "fahrenheit")
        self.assertAlmostEqual(result, 89.6, places = 2)

    def test_fahrenheit_to_kelvin(self):
        result = self.convert(32, "fahrenheit", "kelvin")
        self.assertAlmostEqual(result, 273.15, places = 2)

    def test_kelvin_to_cesius(self):
        result = self.convert(536, "kelvin", "celsius")
        self.assertAlmostEqual(result, 262.85, places = 2)


    # Distance test cases
    def test_meter_to_km(self):
        result = self.convert(62, "meter", "kilometers")
        self.assertAlmostEqual(result, 0.062, places = 2)

    def test_km_to_mile(self):
        result = self.convert(4724, "km", "miles")
        self.assertAlmostEqual(result, 2935.358, places = 1)

    def test_mile_to_yard(self):
        result = self.convert(70.1, "mi", "yards")
        self.assertAlmostEqual(result,  123375.69, places = 1)

    def test_cm_to_inch(self):
        result = self.convert(103, "centimeters", "in")
        self.assertAlmostEqual(result, 40.55, places = 2)

    def test_feet_to_mm(self):
        result = self.convert(2, "ft", "millimeters")
        self.assertAlmostEqual(result, 609.6, places = 2)

    # Weight test cases
    def test_gram_to_oz(self):
        result = self.convert(82, "g", "ounces")
        self.assertAlmostEqual(result, 2.89, places = 2)

    def test_oz_to_mg(self):
        result = self.convert(0.33, "oz", "milligrams")
        self.assertAlmostEqual(result, 9355.3, places = 1)

    def test_lb_to_kg(self):
        result = self.convert(135, "pounds", "kg")
        self.assertAlmostEqual(result, 61.23, places = 2)

    def test_kg_to_oz(self):
        result = self.convert(44, "kilogram", "ounce")
        self.assertAlmostEqual(result, 1552.02, places = 1)

if __name__ == "__main__":
    unittest.main()

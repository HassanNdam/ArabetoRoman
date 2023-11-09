import unittest

def convert_arab_to_roman(decimal):
    if not 1 <= decimal <= 3999:
        raise ValueError("La conversion n'est possible que pour les nombres entre 1 et 3999.")

    roman_numerals = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }

    result = ""
    values = sorted(roman_numerals.keys(), reverse=True)

    for value in values:
        while decimal >= value:
            result += roman_numerals[value]
            decimal -= value

    return result

try:
    decimal_input = int(input("Entrez un nombre Arabe entre 1 et 3999 : "))
    roman_output = convert_arab_to_roman(decimal_input)
    print(f"Le nombre romain correspondant est : {roman_output}")
except ValueError as e:
    print(f"Erreur : {e}")


class TestConvertArabToRoman(unittest.TestCase):
    def test_roman_to_decimal(self):
        # Test avec un chiffre romain valide
        self.assertEqual(convert_arab_to_roman(50), "L")

    def test_roman_to_decimal_invalid(self):
        # Test avec un chiffre romain invalide
        with self.assertRaises(ValueError):
            convert_arab_to_roman(4000)

if __name__ == '__main__':
    unittest.main()

import unittest


def convert_roman_to_arab(roman):
    roman_numerals = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }

    decimal = 0
    prev_value = 0

    for numeral in reversed(roman):
        value = roman_numerals.get(numeral, 0)

        if value < prev_value:
            decimal -= value
        else:
            decimal += value

        prev_value = value

        if decimal > 3999:
            raise ValueError("La conversion n'est possible que pour les nombres entre I et MMMCMXCIX (1 à 3999).")

    return decimal

def input_roman_number():
    while True:
        try:
            roman_input = input("Entrez un nombre Romain entre 1 et 3999 : ")
            # Vérifiez si l'entrée est composée de chiffres romains valides
            if all(char in "IVXLCDM" for char in roman_input):
                return roman_input
            else:
                print("L'entrée n'est pas un chiffre romain valide. Veuillez réessayer.")
        except ValueError:
            print("Erreur : L'entrée n'est pas un chiffre romain valide.")

try:
    roman_input = input_roman_number()
    decimal_output = convert_roman_to_arab(roman_input)
    print(f"Le nombre romain correspondant est : {decimal_output}")
except ValueError as e:
    print(f"Erreur : {e}")


class TestConvertRomanToArab(unittest.TestCase):
    def test_roman_to_arab(self):
        # Test avec un chiffre romain valide
        self.assertEqual(convert_roman_to_arab("L"), 50)

    def test_roman_to_arab_invalid(self):
        # Test avec un chiffre romain invalide
        with self.assertRaises(ValueError):
            convert_roman_to_arab("MMMM")

if __name__ == '__main__':
    unittest.main()
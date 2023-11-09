def convert_roman_to_decimal(roman):
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


print(convert_roman_to_decimal("VIII"))

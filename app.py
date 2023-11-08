
from flask import Flask, request, jsonify, render_template

app = Flask(__name)

def convert_decimal_to_roman(decimal):
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

print(convert_decimal_to_roman(4000))
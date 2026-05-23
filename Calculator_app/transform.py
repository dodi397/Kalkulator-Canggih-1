
import math

BASE_MAP = {
    "decimal": 10,
    "binary": 2,
    "octal": 8,
    "hexadecimal": 16,
}

CURRENCY_RATES = {
    "IDR": 1.0,
    "USD": 16000.0,
    "EUR": 17500.0,
    "SGD": 11800.0,
    "MYR": 3400.0,
    "JPY": 108.0,
    "GBP": 20000.0,
}

def format_number(value):
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    if isinstance(value, float):
        return f"{value:.6f}".rstrip("0").rstrip(".")
    return str(value)

def convert_base(value_text, from_base, to_base):
    from_base_num = BASE_MAP[from_base]
    to_base_num = BASE_MAP[to_base]
    n = int(value_text, from_base_num)

    if to_base_num == 10:
        result = str(n)
    elif to_base_num == 2:
        result = bin(n)[2:]
    elif to_base_num == 8:
        result = oct(n)[2:]
    elif to_base_num == 16:
        result = hex(n)[2:].upper()

    steps = [
        f"Baca {value_text} sebagai bilangan basis {from_base_num}.",
        f"Ubah ke desimal: {value_text}({from_base_num}) = {n}(10).",
        f"Konversi dari desimal ke basis {to_base_num}.",
        f"Hasil = {result}({to_base_num}).",
    ]
    formula = f"{value_text} ({from_base.upper()}) → {result} ({to_base.upper()})"
    return {"result": result, "formula": formula, "expression": formula, "steps": steps}

def to_celsius(value, unit):
    if unit == "celsius":
        return value
    if unit == "fahrenheit":
        return (value - 32) * 5 / 9
    if unit == "kelvin":
        return value - 273.15
    if unit == "reamur":
        return value * 5 / 4
    raise ValueError("Unit suhu tidak dikenali.")

def from_celsius(value, unit):
    if unit == "celsius":
        return value
    if unit == "fahrenheit":
        return value * 9 / 5 + 32
    if unit == "kelvin":
        return value + 273.15
    if unit == "reamur":
        return value * 4 / 5
    raise ValueError("Unit suhu tidak dikenali.")

def convert_temperature(value, from_unit, to_unit):
    c = to_celsius(value, from_unit)
    result = from_celsius(c, to_unit)
    steps = [
        f"Ubah {format_number(value)} {from_unit.title()} ke Celsius.",
        f"Nilai antara = {format_number(c)} °C.",
        f"Konversi dari Celsius ke {to_unit.title()}.",
        f"Hasil = {format_number(result)} {to_unit.title()}."
    ]
    formula = f"{format_number(value)} {from_unit.title()} → {format_number(result)} {to_unit.title()}"
    return {"result": result, "formula": formula, "expression": formula, "steps": steps}

def convert_currency(amount, from_currency, to_currency):
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()
    if from_currency not in CURRENCY_RATES or to_currency not in CURRENCY_RATES:
        raise ValueError("Mata uang tidak dikenali.")

    amount_idr = amount * CURRENCY_RATES[from_currency]
    result = amount_idr / CURRENCY_RATES[to_currency]
    steps = [
        f"Jadikan nilai awal ke IDR: {format_number(amount)} {from_currency} = {format_number(amount_idr)} IDR.",
        f"Bagi dengan rate {to_currency}: 1 {to_currency} = {format_number(CURRENCY_RATES[to_currency])} IDR.",
        f"Hasil = {format_number(result)} {to_currency}."
    ]
    formula = f"{format_number(amount)} {from_currency} → {format_number(result)} {to_currency}"
    return {"result": result, "formula": formula, "expression": formula, "steps": steps}

def factorial_steps(n):
    if n < 0:
        raise ValueError("Faktorial hanya untuk bilangan bulat non-negatif.")
    result = math.factorial(n)
    chain = " × ".join(str(i) for i in range(n, 0, -1)) if n > 1 else "1"
    steps = [
        f"Tulis {n}! sebagai perkalian menurun.",
        f"{n}! = {chain}.",
        f"Hasil = {result}."
    ]
    formula = f"{n}!"
    return {"result": result, "formula": formula, "expression": formula, "steps": steps}

def fibonacci_series(n):
    if n <= 0:
        raise ValueError("Jumlah deret Fibonacci harus lebih dari 0.")
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    steps = [
        "Mulai dari 0 dan 1.",
        "Setiap suku adalah jumlah dua suku sebelumnya.",
        f"{n} suku pertama: {', '.join(map(str, series))}."
    ]
    formula = f"Fibonacci {n} suku"
    return {"result": series, "formula": formula, "expression": formula, "steps": steps}

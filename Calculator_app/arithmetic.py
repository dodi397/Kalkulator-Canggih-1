import math

def format_number(value):
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    if isinstance(value, float):
        return f"{value:.6f}".rstrip("0").rstrip(".")
    return str(value)

def calculate_arithmetic(op, a, b=None):
    steps = []
    if op == "sqrt":
        if a < 0:
            raise ValueError("Akar dari bilangan negatif tidak diperbolehkan.")
        result = math.sqrt(a)
        steps = [
            f"Ambil nilai akar dari {format_number(a)}.",
            f"Cari bilangan yang jika dikuadratkan menghasilkan {format_number(a)}.",
            f"Hasilnya adalah {format_number(result)}."
        ]
        formula = f"√({format_number(a)})"
        expression = formula
    elif op == "pow":
        result = a ** b
        steps = [
            f"Nilai basis = {format_number(a)}.",
            f"Nilai pangkat = {format_number(b)}.",
            f"Hitung perkalian berulang sebanyak {format_number(b)} kali.",
            f"Hasil akhir = {format_number(result)}."
        ]
        formula = f"{format_number(a)} ^ {format_number(b)}"
        expression = formula
    elif op == "mod":
        if b == 0:
            raise ZeroDivisionError("Modulus dengan nol tidak diperbolehkan.")
        result = a % b
        steps = [
            f"Bagi {format_number(a)} dengan {format_number(b)}.",
            f"Ambil sisa pembagian.",
            f"Sisa = {format_number(result)}."
        ]
        formula = f"{format_number(a)} mod {format_number(b)}"
        expression = formula
    elif op == "floordiv":
        if b == 0:
            raise ZeroDivisionError("Pembagian dengan nol tidak diperbolehkan.")
        result = a // b
        steps = [
            f"Bagi {format_number(a)} dengan {format_number(b)}.",
            f"Ambil hasil pembagian bulat ke bawah.",
            f"Hasil = {format_number(result)}."
        ]
        formula = f"{format_number(a)} // {format_number(b)}"
        expression = formula
    elif op == "add":
        result = a + b
        steps = [
            f"Jumlahkan {format_number(a)} dan {format_number(b)}.",
            f"{format_number(a)} + {format_number(b)} = {format_number(result)}."
        ]
        formula = f"{format_number(a)} + {format_number(b)}"
        expression = formula
    elif op == "sub":
        result = a - b
        steps = [
            f"Kurangkan {format_number(b)} dari {format_number(a)}.",
            f"{format_number(a)} - {format_number(b)} = {format_number(result)}."
        ]
        formula = f"{format_number(a)} - {format_number(b)}"
        expression = formula
    elif op == "mul":
        result = a * b
        steps = [
            f"Kalikan {format_number(a)} dengan {format_number(b)}.",
            f"{format_number(a)} × {format_number(b)} = {format_number(result)}."
        ]
        formula = f"{format_number(a)} × {format_number(b)}"
        expression = formula
    elif op == "div":
        if b == 0:
            raise ZeroDivisionError("Pembagian dengan nol tidak diperbolehkan.")
        result = a / b
        steps = [
            f"Bagi {format_number(a)} dengan {format_number(b)}.",
            f"{format_number(a)} ÷ {format_number(b)} = {format_number(result)}."
        ]
        formula = f"{format_number(a)} ÷ {format_number(b)}"
        expression = formula
    else:
        raise ValueError("Operator tidak dikenali.")

    return {"result": result, "formula": formula, "expression": expression, "steps": steps}

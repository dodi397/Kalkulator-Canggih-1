def to_bool(value):
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return bool(int(value))
    text = str(value).strip().lower()
    return text in ("1", "true", "t", "yes", "y", "on", "benar")

def logic_label(val):
    return "TRUE" if val else "FALSE"

def calculate_logic(op, a, b=None):
    a_bool = to_bool(a)
    b_bool = to_bool(b) if b is not None else None
    steps = []

    if op == "not":
        result = not a_bool
        steps = [
            f"Nilai input A = {logic_label(a_bool)}.",
            "Operasi NOT membalik nilai logika.",
            f"Hasil = {logic_label(result)}."
        ]
        formula = f"NOT {logic_label(a_bool)}"
        expression = formula
    else:
        if b_bool is None:
            raise ValueError("Operasi logika ini membutuhkan dua input.")
        if op == "and":
            result = a_bool and b_bool
            op_text = "AND"
        elif op == "or":
            result = a_bool or b_bool
            op_text = "OR"
        elif op == "xor":
            result = (a_bool and not b_bool) or (not a_bool and b_bool)
            op_text = "XOR"
        elif op == "nand":
            result = not (a_bool and b_bool)
            op_text = "NAND"
        elif op == "nor":
            result = not (a_bool or b_bool)
            op_text = "NOR"
        else:
            raise ValueError("Operator logika tidak dikenali.")

        steps = [
            f"Nilai A = {logic_label(a_bool)}.",
            f"Nilai B = {logic_label(b_bool)}.",
            f"Terapkan operator {op_text}.",
            f"Hasil = {logic_label(result)}."
        ]
        formula = f"{logic_label(a_bool)} {op_text} {logic_label(b_bool)}"
        expression = formula

    return {"result": result, "formula": formula, "expression": expression, "steps": steps}

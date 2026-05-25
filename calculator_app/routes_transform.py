from flask import Blueprint, render_template, request
from calculator_app.transform import (
    convert_base,
    convert_temperature,
    convert_currency,
    factorial_steps,
    fibonacci_series,
    format_number,
)
from calculator_app.history import add_history, get_history

transform_bp = Blueprint("transform", __name__)

@transform_bp.route("/", methods=["GET", "POST"])
def transform_page():
    result = None
    error = None
    form = {
        "mode": "base",
        "value": "",
        "from_unit": "decimal",
        "to_unit": "binary",
        "temp_from": "celsius",
        "temp_to": "fahrenheit",
        "currency_from": "IDR",
        "currency_to": "USD",
        "n": "5",
    }

    if request.method == "POST":
        form.update({
            "mode": request.form.get("mode", "base"),
            "value": request.form.get("value", "").strip(),
            "from_unit": request.form.get("from_unit", "decimal"),
            "to_unit": request.form.get("to_unit", "binary"),
            "temp_from": request.form.get("temp_from", "celsius"),
            "temp_to": request.form.get("temp_to", "fahrenheit"),
            "currency_from": request.form.get("currency_from", "IDR"),
            "currency_to": request.form.get("currency_to", "USD"),
            "n": request.form.get("n", "5"),
        })

        try:
            mode = form["mode"]
            if mode == "base":
                calc = convert_base(form["value"], form["from_unit"], form["to_unit"])
                add_history("Transformasi Bilangan", calc["expression"], calc["result"], "Konversi basis berhasil.")
            elif mode == "temperature":
                value = float(form["value"])
                calc = convert_temperature(value, form["temp_from"], form["temp_to"])
                add_history("Transformasi Bilangan", calc["expression"], format_number(calc["result"]), "Konversi suhu berhasil.")
            elif mode == "currency":
                value = float(form["value"])
                calc = convert_currency(value, form["currency_from"], form["currency_to"])
                add_history("Transformasi Bilangan", calc["expression"], format_number(calc["result"]), "Konversi mata uang berhasil.")
            elif mode == "factorial":
                n = int(float(form["n"] if form["n"] else form["value"] or "0"))
                calc = factorial_steps(n)
                add_history("Transformasi Bilangan", calc["expression"], format_number(calc["result"]), "Faktorial berhasil dihitung.")
            elif mode == "fibonacci":
                n = int(float(form["n"] if form["n"] else form["value"] or "0"))
                calc = fibonacci_series(n)
                add_history("Transformasi Bilangan", calc["expression"], ", ".join(map(str, calc["result"])), "Deret Fibonacci berhasil dibuat.")
            else:
                raise ValueError("Mode transformasi tidak dikenali.")

            result = {
                "value": calc["result"],
                "formula": calc["formula"],
                "steps": calc["steps"],
                "category": "Transformasi Bilangan",
            }
        except Exception as exc:
            error = str(exc)

    return render_template("transform.html", active_page="transform", page_kicker="Transformasi Bilangan", page_title="Transformasi Bilangan", result=result, error=error, form=form, history=get_history())


from flask import Blueprint, render_template, request
from calculator_app.arithmetic import calculate_arithmetic, format_number
from calculator_app.history import add_history, get_history

arithmetic_bp = Blueprint("arithmetic", __name__)

@arithmetic_bp.route("/", methods=["GET", "POST"])
def arithmetic_page():
    result = None
    error = None
    form = {"a": "", "b": "", "op": "add"}

    if request.method == "POST":
        form["a"] = request.form.get("a", "").strip()
        form["b"] = request.form.get("b", "").strip()
        form["op"] = request.form.get("op", "add").strip()

        try:
            a = float(form["a"])
            op = form["op"]
            b = float(form["b"]) if form["b"] != "" else None
            calc = calculate_arithmetic(op, a, b)
            result_value = calc["result"]
            result = {
                "value": format_number(result_value),
                "formula": calc["formula"],
                "steps": calc["steps"],
                "category": "Operasi Aritmatika",
            }
            add_history("Operasi Aritmatika", calc["expression"], format_number(result_value), "Berhasil menghitung operasi aritmatika.")
        except Exception as exc:
            error = str(exc)

    return render_template("arithmetic.html", active_page="arith", page_kicker="Operasi Aritmatika", page_title="Operasi Aritmatika", result=result, error=error, form=form, history=get_history())

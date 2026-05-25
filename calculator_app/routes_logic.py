
from flask import Blueprint, render_template, request
from calculator_app.logic import calculate_logic, logic_label
from calculator_app.history import add_history, get_history

logic_bp = Blueprint("logic", __name__)

@logic_bp.route("/", methods=["GET", "POST"])
def logic_page():
    result = None
    error = None
    form = {"a": "1", "b": "0", "op": "and"}

    if request.method == "POST":
        form["a"] = request.form.get("a", "1").strip()
        form["b"] = request.form.get("b", "0").strip()
        form["op"] = request.form.get("op", "and").strip()

        try:
            op = form["op"]
            a = form["a"]
            b = form["b"]
            calc = calculate_logic(op, a, b if op != "not" else None)
            result_value = calc["result"]
            result = {
                "value": logic_label(result_value),
                "formula": calc["formula"],
                "steps": calc["steps"],
                "category": "Operator Logika",
            }
            add_history("Operator Logika", calc["expression"], logic_label(result_value), "Berhasil menghitung operator logika.")
        except Exception as exc:
            error = str(exc)

    return render_template("logic.html", active_page="logic", page_kicker="Operator Logika", page_title="Operator Logika", result=result, error=error, form=form, history=get_history())

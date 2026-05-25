from flask import Blueprint, render_template, session, redirect, request, url_for
from calculator_app.history import get_history

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    history = get_history()
    return render_template(
        "index.html",
        history=history,
        active_page="home",
        page_kicker="Dashboard",
        page_title="Selamat datang di SmartCalc Pro! 👋",
    )

@main_bp.route("/clear-history", methods=["POST"])
def clear_history():
    session["history"] = []
    session.modified = True
    return redirect(request.referrer or url_for("main.index"))

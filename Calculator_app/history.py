
from flask import session
from datetime import datetime

def init_session_history():
    if "history" not in session:
        session["history"] = []

def add_history(category, expression, result, detail):
    init_session_history()
    items = session["history"]
    items.insert(0, {
        "time": datetime.now().strftime("%H:%M:%S"),
        "category": category,
        "expression": expression,
        "result": result,
        "detail": detail,
    })
    session["history"] = items[:10]
    session.modified = True

def get_history():
    init_session_history()
    return session["history"]

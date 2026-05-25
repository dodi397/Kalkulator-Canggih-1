from flask import Flask
from calculator_app.routes_main import main_bp
from calculator_app.routes_arithmetic import arithmetic_bp
from calculator_app.routes_logic import logic_bp
from calculator_app.routes_transform import transform_bp
from calculator_app.history import init_session_history

app = Flask(__name__)
app.secret_key = "smartcalc-pro-secret-key-change-me"

app.register_blueprint(main_bp)
app.register_blueprint(arithmetic_bp, url_prefix="/aritmatika")
app.register_blueprint(logic_bp, url_prefix="/logika")
app.register_blueprint(transform_bp, url_prefix="/transformasi")

#@app.before_request
#def ensure_history():
#    init_session_history()

@app.route("/")
def home():
    return "Flask berjalan di Vercel!"
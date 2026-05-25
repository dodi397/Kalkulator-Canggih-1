import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, BASE_DIR)

from flask import Flask
from calculator_app.routes_main import main_bp
from calculator_app.routes_arithmetic import arithmetic_bp
from calculator_app.routes_logic import logic_bp
from calculator_app.routes_transform import transform_bp

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

app.secret_key = "secret"

app.register_blueprint(main_bp)
app.register_blueprint(arithmetic_bp)
app.register_blueprint(logic_bp)
app.register_blueprint(transform_bp)

@app.route("/")
def home():
    return "Website berhasil deploy!"

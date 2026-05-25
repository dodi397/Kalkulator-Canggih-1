import os
import sys
import traceback

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, BASE_DIR)

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    try:
        from calculator_app.routes_main import main_bp
        from calculator_app.routes_arithmetic import arithmetic_bp
        from calculator_app.routes_logic import logic_bp
        from calculator_app.routes_transform import transform_bp

        app.register_blueprint(main_bp)
        app.register_blueprint(arithmetic_bp)
        app.register_blueprint(logic_bp)
        app.register_blueprint(transform_bp)

        return "Berhasil!"
    except Exception:
        return "<pre>" + traceback.format_exc() + "</pre>", 500
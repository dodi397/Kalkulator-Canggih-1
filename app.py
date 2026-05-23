from flask import Flask
from calculator_app.routes_main import main_bp
from calculator_app.routes_arithmetic import arithmetic_bp
from calculator_app.routes_logic import logic_bp
from calculator_app.routes_transform import transform_bp
from calculator_app.history import init_session_history

def create_app():
    app = Flask(__name__)
    app.secret_key = "smartcalc-pro-secret-key-change-me"

    app.register_blueprint(main_bp)
    app.register_blueprint(arithmetic_bp, url_prefix="/aritmatika")
    app.register_blueprint(logic_bp, url_prefix="/logika")
    app.register_blueprint(transform_bp, url_prefix="/transformasi")

    @app.before_request
    def ensure_history():
        init_session_history()

    return app

app = create_app()

if __name__ == "__main__":
       app.run(host="0.0.0.0", port=8000, debug=True)
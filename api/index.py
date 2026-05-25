from flask import Flask
from calculator_app.routes_main import main_bp
from calculator_app.routes_arithmetic import arithmetic_bp
from calculator_app.routes_logic import logic_bp
from calculator_app.routes_transform import transform_bp
from calculator_app.history import init_session_history

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

app.secret_key = "secret"

init_session_history(app)

app.register_blueprint(main_bp)
app.register_blueprint(arithmetic_bp)
app.register_blueprint(logic_bp)
app.register_blueprint(transform_bp)

@app.route("/")
def home():
    return "Website berhasil deploy!"
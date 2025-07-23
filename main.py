from flask import Flask
from blueprints.auth.login import login_bp
from blueprints.register.register import reg_bp
from blueprints.list.list import list_bp
from blueprints.users.users import users_bp

# from blueprints.register.register import reg_bp

app = Flask(__name__)
app.secret_key = "secret"
app.register_blueprint(login_bp, url_prefix="/login")
app.register_blueprint(reg_bp)
app.register_blueprint(list_bp)
app.register_blueprint(users_bp)


if __name__ == "__main__":
    app.run(debug=True)

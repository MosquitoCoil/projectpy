from flask import Flask  # render_template
from Backend.auth.login import login_bp
from Backend.routes.user_list import user_list_bp
from Backend.routes.delete_user import del_user_bp
from Backend.routes.edit_user import edit_user_bp

# from blueprints.auth.login import login_bp
from Backend.auth.register import reg_bp
from Backend.routes.users import users_bp

# from blueprints.register.register import reg_bp

app = Flask(__name__)

app.secret_key = "secret"
app.register_blueprint(login_bp, url_prefix="/login")
app.register_blueprint(reg_bp)
app.register_blueprint(user_list_bp)
app.register_blueprint(del_user_bp)
app.register_blueprint(edit_user_bp)
app.register_blueprint(users_bp)


"""@app.route("/")
def main():
    return render_template("base.html")"""


if __name__ == "__main__":
    app.run(debug=True)

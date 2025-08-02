from flask import Flask
from flask_cors import CORS
from Backend.auth.login import login_bp
from Backend.auth.register import reg_bp
from Backend.routes.user_list import user_list_bp
from Backend.routes.delete_user import del_user_bp
from Backend.routes.edit_user import edit_user_bp
from Backend.routes.add_user import add_user_bp
from Backend.routes.users import users_bp

# in API

from Backend.api.login import login_api
from Backend.api.register import register_api
from Backend.api.user_list import user_list_api
from Backend.api.add_user import add_user_api
from Backend.api.edit_user import edit_user_api
from Backend.api.delete_user import delete_user_api

app = Flask(__name__)
CORS(app)

app.secret_key = "secret"

# Register blueprint for python flask
app.register_blueprint(login_bp, url_prefix="/login")
app.register_blueprint(reg_bp)
app.register_blueprint(user_list_bp)
app.register_blueprint(del_user_bp)
app.register_blueprint(edit_user_bp)
app.register_blueprint(add_user_bp)
app.register_blueprint(users_bp)
# Register blueprint for react-native app
app.register_blueprint(login_api, url_prefix="/api")
app.register_blueprint(register_api, url_prefix="/api")
app.register_blueprint(user_list_api, url_prefix="/api")
app.register_blueprint(add_user_api, url_prefix="/api")
app.register_blueprint(edit_user_api, url_prefix="/api")
app.register_blueprint(delete_user_api, url_prefix="/api")


@app.route("/")
def main():
    return {"message": "API Running"}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

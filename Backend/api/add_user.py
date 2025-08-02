from flask import Blueprint, request, jsonify
from database.db import get_db_connection
from werkzeug.security import generate_password_hash

add_user_api = Blueprint("add_user_api", __name__)


# add user in react-native app
@add_user_api.route("/add-user", methods=["POST"])
def add_user():
    data = request.json
    firstname = data.get("firstname")
    lastname = data.get("lastname")
    username = data.get("username")
    password = data.get("password")
    is_admin = data.get("is_admin", 0)

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (firstname, lastname, username, password, is_admin) VALUES (%s, %s, %s, %s, %s)",
        (
            firstname,
            lastname,
            username,
            generate_password_hash(password),
            is_admin,
        ),
    )
    conn.commit()
    conn.close()

    return jsonify({"success": True, "message": "User registered"})

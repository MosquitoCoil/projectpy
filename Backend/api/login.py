from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from database.db import get_db_connection

login_api = Blueprint("login_api", __name__)


# React Native login route
@login_api.route("/login", methods=["POST"])
def api_login():
    data = request.get_json()

    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Missing username or password"}), 400

    username = data["username"]
    password = data["password"]

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    conn.close()

    if user and check_password_hash(user["password"], password):
        # is_admin ('admin' or 'user')
        is_admin = user["is_admin"]  # 'admin' or 'user'

        return (
            jsonify(
                {
                    "success": True,
                    "message": "Login successful",
                    "user": {
                        "id": user["id"],
                        "username": user["username"],
                        "firstname": user["firstname"],
                        "is_admin": is_admin,
                    },
                }
            ),
            200,
        )

    else:
        return (
            jsonify({"success": False, "message": "Invalid username or password"}),
            401,
        )

from flask import Blueprint, request, jsonify
from database.db import get_db_connection
from werkzeug.security import generate_password_hash

edit_user_api = Blueprint("edit_user_api", __name__)


# edit user in react-native app
@edit_user_api.route("/edit-user/<int:user_id>", methods=["PUT"])
def edit_user(user_id):
    data = request.get_json()
    firstname = data["firstname"]
    lastname = data["lastname"]
    username = data["username"]
    is_admin = data["is_admin"]
    password = data.get("password", "")

    conn = get_db_connection()
    cursor = conn.cursor()

    if password.strip() != "":
        # Only hash if a real password is provided
        new_password = generate_password_hash(password)
        cursor.execute(
            "UPDATE users SET firstname=%s, lastname=%s, username=%s, password=%s, is_admin=%s WHERE id=%s",
            (firstname, lastname, username, new_password, is_admin, user_id),
        )
    else:
        # Keep existing password
        cursor.execute(
            "UPDATE users SET firstname=%s, lastname=%s, username=%s, is_admin=%s WHERE id=%s",
            (firstname, lastname, username, is_admin, user_id),
        )

    conn.commit()
    conn.close()
    return jsonify({"success": True, "message": "User updated"})

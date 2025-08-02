from flask import Blueprint, request, jsonify
from database.db import get_db_connection
from werkzeug.security import generate_password_hash
import mysql.connector

register_api = Blueprint("register_api", __name__)


# for react-native app registration
@register_api.route("/register", methods=["POST"])
def api_register():
    data = request.json

    firstname = data.get("firstname")
    lastname = data.get("lastname")
    username = data.get("username")
    password = data.get("password")
    is_admin = data.get("is_admin", 0)

    if not (firstname and lastname and username and password):
        return jsonify({"success": False, "message": "All fields are required."}), 400

    hashed_pw = generate_password_hash(password)

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (firstname, lastname, username, password, is_admin) VALUES (%s, %s, %s, %s, %s)",
            (firstname, lastname, username, hashed_pw, is_admin),
        )
        conn.commit()
        return jsonify({"success": True, "message": "Registered Successfully!"}), 201
    except mysql.connector.Error as err:
        return jsonify({"success": False, "message": str(err)}), 500
    finally:
        conn.close()

from flask import Blueprint, jsonify
from database.db import get_db_connection

user_list_api = Blueprint("user_list_api", __name__)


# for react-native app
@user_list_api.route("/users", methods=["GET"])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, firstname, lastname, username, is_admin FROM users")
    users = cursor.fetchall()
    conn.close()
    return jsonify({"users": users})

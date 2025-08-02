from flask import Blueprint, jsonify
from database.db import get_db_connection

delete_user_api = Blueprint("delete_user_api", __name__)


# delete user in react-native app
@delete_user_api.route("/delete-user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()
    conn.close()
    return jsonify({"success": True, "message": "User deleted successfully"})

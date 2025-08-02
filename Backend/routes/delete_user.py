from flask import Blueprint, redirect, session, flash
from database.db import get_db_connection

del_user_bp = Blueprint(
    "delete", __name__, template_folder="../../Frontend/admin/templates"
)


# delete user
@del_user_bp.route("/delete_user/<int:user_id>", methods=["POST", "GET"])
def delete_user(user_id):
    if not session.get("is_admin"):
        flash("Admin access only.", "error")
        return redirect("/login")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()
    conn.close()

    flash("User deleted successfully.", "error")
    return redirect("/list")

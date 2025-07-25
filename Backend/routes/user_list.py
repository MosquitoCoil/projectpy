from flask import render_template, Blueprint, session, flash, redirect
from database.db import get_db_connection

user_list_bp = Blueprint(
    "list", __name__, template_folder="../../Frontend/admin/templates"
)


@user_list_bp.route("/list")
def list():
    if not session.get("is_admin"):
        flash("Admin access only.", "error")
        return redirect("/login")

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT id, firstname, lastname, username, timecreated, is_admin FROM users"
    )
    users = cursor.fetchall()
    conn.close()

    return render_template("user_list.html", users=users)

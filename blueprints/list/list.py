from flask import render_template, redirect, Blueprint, session
from database.db import get_db_connection

list_bp = Blueprint("list", __name__, template_folder="templates")


@list_bp.route("/list")
def list():
    if not session.get("is_admin"):
        return "<h1>You're not an admin</h1>"
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, firstname, username, timecreated FROM users")
    users = cursor.fetchall()
    conn.close()

    return render_template("user_list.html", users=users, title="Registered User List")

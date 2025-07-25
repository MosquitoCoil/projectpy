from flask import Blueprint, redirect, session, request, flash, render_template
from database.db import get_db_connection
from werkzeug.security import generate_password_hash

add_user_bp = Blueprint(
    "add", __name__, template_folder="../../Frontend/admin/templates"
)


# edit users
@add_user_bp.route("/add-user", methods=["GET", "POST"])
def add_user():
    if not session.get("is_admin"):
        flash("Admin access only.", "error")
        return redirect("/login")

    if request.method == "POST":
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        username = request.form["username"]
        password = request.form["password"]
        is_admin = request.form.get("is_admin", 0)

        # Encrypt password
        hashed_password = generate_password_hash(password)

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (firstname, lastname, username, password, is_admin) VALUES (%s, %s, %s, %s, %s)",
            (firstname, lastname, username, hashed_password, is_admin),
        )
        conn.commit()
        cursor.close()
        conn.close()

        flash("User successfully added!", "success")
        return redirect("/list")

    return render_template("add_user.html", user=None)

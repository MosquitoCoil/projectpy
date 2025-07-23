from flask import Blueprint, render_template, request, session, redirect, flash
from database.db import get_db_connection
from werkzeug.security import check_password_hash
from datetime import datetime

login_bp = Blueprint(
    "login", __name__, static_folder="static", template_folder="templates"
)


@login_bp.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user["password"], password):
            session["username"] = user["username"]
            session["is_admin"] = user["is_admin"]
            session["firstname"] = user["firstname"]
            login_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            flash(f"Welcome, {user["firstname"]}! Logged in at {login_time}")

            if user["is_admin"]:
                return redirect("/list")
            else:
                return redirect("/dashboard")
        else:
            return redirect("/login")

    return render_template("login.html")


@login_bp.route("/logout")
def logout():
    print("Logging out...")
    session.clear()
    return redirect("/login")

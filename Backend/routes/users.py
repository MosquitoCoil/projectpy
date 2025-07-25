from flask import Blueprint, render_template, session, flash, redirect

users_bp = Blueprint("users", __name__, template_folder="../../Frontend/user/templates")


@users_bp.route("/dashboard")
def users():
    if session.get("is_admin") != "user":
        flash("Access denied: Users only", "error")
        return redirect("/login")

    return render_template("user_dashboard.html")

from flask import Blueprint, render_template

users_bp = Blueprint("users", __name__, template_folder="../../Frontend/user/templates")


@users_bp.route("/dashboard")
def users():
    return render_template("user_dashboard.html")

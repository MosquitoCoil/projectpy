from flask import Blueprint, redirect, session, request, flash, render_template
from database.db import get_db_connection
from werkzeug.security import generate_password_hash

edit_user_bp = Blueprint(
    "edit", __name__, template_folder="../../Frontend/admin/templates"
)


# edit users
@edit_user_bp.route("/edit-user/<int:user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    if not session.get("is_admin"):
        flash("Admin access only.", "error")
        return redirect("/login")

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "POST":
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        username = request.form["username"]
        is_admin = request.form["is_admin"]
        password = request.form["password"]
        # update password
        new_password = generate_password_hash(password)

        cursor.execute(
            "UPDATE users SET firstname = %s, lastname = %s, username = %s, password = %s, is_admin = %s WHERE id = %s",
            (firstname, lastname, username, new_password, is_admin, user_id),
        )
        conn.commit()
        conn.close()
        flash("User updated successfully.", "success")
        return redirect("/list")

    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    conn.close()

    return render_template("edit_user.html", user=user)

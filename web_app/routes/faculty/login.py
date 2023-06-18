from flask import (
    render_template, 
    session, 
    redirect, 
    url_for, 
    current_app,
    flash
    )
from passlib.hash import pbkdf2_sha256
from web_app.forms import LoginForm
from web_app.models import User
from web_app.routes.faculty import faculty_bp


#-------------------- LOGIN ROUTES ------------------------


# LOGIN ROUTE

@faculty_bp.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        user_data = current_app.db.users.find_one({"info.email" : login_form.email.data}, {"_id" : False}).get('info')
        
        if not user_data:
            flash("Login credentials are incorrect.", category="danger")
            return redirect(url_for("login"))
        user = User(**user_data)

        if user and pbkdf2_sha256.verify(login_form.password.data, user.password):
            session['user_id'] = user.id
            session['email'] = user.email

            return redirect(url_for('index.index'))
        
        flash("Login credentials are incorrect.", category="danger")

    return render_template(
        "faculty/login.html", 
        login_form=login_form)



# LOGOUT ENDPOINT

@faculty_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('faculty.login'))


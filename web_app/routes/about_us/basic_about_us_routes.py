from flask import current_app, render_template
from web_app.routes.about_us import about_us_bp


#-------------------- SIMPLE ROUTES ------------------------


# OUR TEAM ROUTE

@about_us_bp.route("/our_team")
def our_team():
    return render_template(
        "/about_us/our_team.html",
        employees=current_app.db.employees.find({}, {"_id": False})
        )


# OUR COMPANY ROUTE

@about_us_bp.route("/our_company_mindset")
def our_company_mindset():
    return render_template(
        "/about_us/our_company_mindset.html"
        )
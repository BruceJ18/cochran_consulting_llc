from flask import render_template, request, current_app

from web_app.routes.faculty import faculty_bp


@faculty_bp.route('/add_or_edit', methods=["GET", "POST"])
def add_or_edit():


    if request.method == "POST":
        collection = request.form.get("javascript_data")
        entities = current_app.db[collection].find({})


        return render_template(
            "faculty/web_app_mods/add_or_edit.html",
            entities=entities
        )
    

    return render_template(
        "faculty/web_app_mods/add_or_edit.html"

    )

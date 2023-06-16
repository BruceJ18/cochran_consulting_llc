from flask import render_template
from web_app.routes.resources import resources_bp 


#-------------------- BASIC ROUTES ------------------------


# OUR BOOKS ROUTE

@resources_bp.route('/our_books')
def our_books():
    return render_template(
        "/resources/our_books.html"
        )


# OUR NON PROFITS ROUTE

@resources_bp.route('/our_nprfts')
def our_nprfts():
    return render_template(
        "/resources/our_nprfts.html"
        )


# Z - SCORE ROUTE

@resources_bp.route('/z_score')
def z_score():
    return render_template("/resources/z_score.html")
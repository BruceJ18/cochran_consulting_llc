from flask import render_template, current_app
from web_app.routes.listings import listings_bp


#-------------------- SIMPLE ROUTES ------------------------


# BUSINESS LISTINGS ROUTE

@listings_bp.route('/business_listings')
def business_listings():
    return render_template(
        "/listings/business_listings.html",
        businesses=current_app.db.businesses.find({}, {"_id": False})
        )


# REAL ESTATE LISTINGS ROUTE

@listings_bp.route('/real-estate_listings')
def real_estate_listings():
    return render_template(
        "/listings/real_estate_listings.html",
        real_estate=current_app.db.real_estate.find({}, {"_id":False})
        )
from flask import Blueprint, render_template, current_app, redirect, url_for
from web_app.forms import Client_Form_Index
import smtplib
from web_app.routes.listings import listings_bp
from web_app.routes.resources import resources_bp
from web_app.routes.about_us import about_us_bp
from web_app.routes.faculty import faculty_bp


# -------------- INDEX BLUEPRINT ------------------

index_bp = Blueprint(
    'index',
    __name__,
    template_folder='templates',
    static_folder='static'
)


# INDEX ROUTE

@index_bp.route("/", methods=["GET", "POST"])
def index():
    client_form : Client_Form_Index = Client_Form_Index()
    

    if client_form.validate_on_submit():
        sender: str = current_app.config['EMAIL']
        pswrd: str = current_app.config['PSWRD']
        port: int = current_app.config['PORT']
        print(sender, pswrd, port)
        host = "smtp.gmail.com"
        subject = f" Client, {client_form.name.data} form submission."
        body = f'''

        ** CLIENT CONTACT INFO BELOW **

        Client information:

        name : {client_form.name.data}

        email : {client_form.email.data}

        cell : {client_form.cell_number.data}

        website: {client_form.website_address.data}

        annual revenue : {client_form.annual_revenue.data}

        questions or comments : \n {client_form.questions_or_comments.data} \n



        ** MUST ADD BUSINESS INFO BELOW THROUGH ROOT ACC ASAP **

        business information:

        business name: {client_form.business_name.data}
        '''
        message = f''' From: {sender}
        
        Subject: {subject}\n
        {body}
        '''

        try:
            server = smtplib.SMTP(host, port)
            server.starttls()
            server.login(sender, pswrd )
            server.sendmail(
                sender,
                sender,
                message
            )
            server.close()
        except:
            print("Mail failed to send.")
        
        return redirect(url_for('.index')) # SUCCESS MESSAGE NEEDED

    return render_template("index.html", client_form=client_form)

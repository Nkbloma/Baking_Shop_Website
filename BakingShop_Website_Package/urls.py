from BakingShop_Website_Package import webapp
from flask import render_template
import os 
from flask import send_from_directory   

@webapp.route('/')
@webapp.route('/home')
def Home_Page():
    return render_template("home_page.html", title="Home") #render static Homepage, unless you want to switch the large icon everynow and then.


@webapp.route('/faq')
def FAQ_Page():
    return render_template("faq_page.html", title="Page") #render static Faq


@webapp.route('/shop')
def Shop_Page():
    return render_template("shop_page.html", title="Shop")  #render unique shop page with shop elements and modifiable template


@webapp.route('/profile')
def Profile_Page():
    return render_template("profile_page.html", title="Profile")  #render Profile template with registered user  

@webapp.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(webapp.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

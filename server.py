"""Server for transit calculation app."""
from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db, db, User
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """View Homepage"""

    return render_template('homepage.html')

@app.route('/results')
def results():
    """Show information based on the user's input on the homepage"""
    origin = request.args.get("origin")
    destination = request.args.get("destination")
    transportation_type = request.args.get("transportation-type")
    frequency = int(request.args.get("frequency"))
    fare_type = request.args.get("fare-type")

    #Determine the cost of the base fare based on transportation type
    if transportation_type == "donkey":
        per_trip_fare = 1
        prepay_fare = 3
    else:
        per_trip_fare = 10
        prepay_fare = 30

    #Calculate the current cost of the weekly trip for the user
    #Compare the cost to determine if the weekly fare is cost effective
    price_efficient = False
    if fare_type == "per-trip":
        current_cost = per_trip_fare*frequency*2
        if transportation_type == "donkey" and current_cost <= 3:
            price_efficient = True
        if transportation_type == "teleportation" and current_cost <= 30:
            price_efficient = True
    else:
        current_cost = prepay_fare
        per_trip_cost = per_trip_fare*frequency*2
        if per_trip_cost >= prepay_fare:
            price_efficient = True

    #Calculate how much the user would save if they switch from an inefficient price
    if price_efficient == False:
        savings = current_cost - prepay_fare

    #Determine if the route is time efficient
    time_efficient = False
    if transportation_type == "teleportation":
        time_efficient = True

    return render_template('results.html',
                            current_cost=current_cost,
                            price_efficient=price_efficient,
                            savings=savings,
                            time_efficient=time_efficient)

@app.route("/login", methods=["GET"])
def show_login():
    """Show login form."""

    return render_template("login.html")


@app.route("/login", methods=["POST"])
def process_login():
    """Log user into site or create user if they do not exist in db.
    """

    email = request.form.get("email")
    password = request.form.get("password")
    #create user function and pass what's inputted
    user = crud.get_user_by_email(email)
    if not user:
        user = crud.create_user(email, password)
        db.session.add(user)
        db.session.commit()

    return redirect("/")

@app.route("/logout")
def process_logout():

    del session["logged_in_user_email"]
    flash("Logged out.")
    return redirect("/")


#login, sign up -> make a form
#go to hope page, there is a login link and a sign up link --> Need to implment an href to /login in header
#sign up link page returns sign up template -> points to /signup
#form to sign up for an account
#separate everything into discrete components


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)




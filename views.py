import json
from flask import Blueprint,render_template,request,jsonify,redirect,url_for,flash

view_blueprint= Blueprint("view", __name__)

with open("data.json", "r") as file:
    data=json.load(file)

@view_blueprint.route("/")
def home():
    # return "<h1>Welcome to Jovin's Page!</h1>"
    return render_template("index.html", data=data) #data=data ensure we can use this in the html file

@view_blueprint.route("/home")
def home1():
    # return "<h1>Welcome to Jovin's Home Page!</h1>"
    return render_template("index.html", data=data)

@view_blueprint.route("/profile/<username>") #<> means special
def profile(username):
    return render_template("index.html", name=username)

@view_blueprint.route("/form", methods=["GET", "POST"])
def vacancy():
    if request.method=="POST":
        name=request.form.get("name")
        email=request.form.get("email")
        phone=request.form.get("phone")
        position=request.form.get("position")
        message=request.form.get("message")

        if not name or not email or not phone or not position or not message:
            flash("Please fill out all fields", "danger")
        else:
            flash("Your application has been submitted succesfully","success")
            return redirect(url_for("view.form"))
    
    return render_template("form.html")

@view_blueprint.route("/form")
def form():
    return render_template("form.html")

@view_blueprint.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method=="POST":
        name=request.form.get("name")
        email=request.form.get("email")
        message=request.form.get("message")
        
        if not name or not email or not message:
            flash("Please fill out all the fields", "danger")
        else:
            flash("Your message has been sent successfully", "success")
            print(f"Received message from {name} ({email}): {message}")
            return redirect(url_for("view.contact"))
    return render_template("contact.html")


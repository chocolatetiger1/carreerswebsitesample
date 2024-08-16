from flask import Blueprint,flash,redirect,render_template,request,url_for

forms_blueprint=Blueprint("forms", __name__)

@forms_blueprint.route("/vacancy", methods=["GET","POST"])
def vacancy():
    if request.method=="POST":
        name=request.form.get("name")
        email=request.form.get("email")
        phone=request.form.get("phone")
        position=request.form.get("position")
        message=request.form.get("message")

        if not all (field in request.form for field in ["name", "email","phone", "position", "message"]):
            flash("Please fill out all fields", "danger")
        else:
            flash("Your application has been successfully submitted", "success")
            print(f"Received message from {name} ({email}: {message} )")
            return redirect(url_for("view.contact"))
        
        return render_template("contacts.html")
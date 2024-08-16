from flask import Flask
from forms import forms_blueprint
from views import view_blueprint

#flask --app app run
app=Flask(__name__)
app.register_blueprint(view_blueprint, url_prefix="/", static_url_path="/static")
app.register_blueprint(forms_blueprint, url_prefix="/forms", static_url_path="/static")

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0")

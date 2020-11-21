from flask import Flask, render_template, url_for, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/codestomp'
db = SQLAlchemy(app)


class Admin(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":

        uname = request.form.get("username")
        pas = request.form.get("password")
        table = Admin.query.filter_by().first()
        if uname == table.username and pas == table.password:
            return render_template("dashboard.html")
    return render_template("login.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/dashboard")
def dashboard():
    tables = Admin.query.filter_by().all()
    return render_template("dashboard.html", tables=tables)


@app.route("/employeemanagement")
def employeemanagement():
    return render_template("employeemanagement.html")


@app.route('/profile')
def profile():
    return render_template('profile.html')


app.run(debug=True)

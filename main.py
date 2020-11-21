from flask import Flask, render_template, url_for, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/codestomp'
db = SQLAlchemy(app)


class Employee(db.Model):
    sno=db.Column(db.Integer, primary_key=True)
    name =db.Column(db.String(30))
    email=db.Column(db.String(30))
    address= db.Column(db.String(50))
    phone= db.Column(db.String(20))


class Admin(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)


class Staff(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":

        uname = request.form.get("username")
        pas = request.form.get("password")
        tables = Admin.query.filter_by().all()
        for table in tables:
            if uname == table.username and pas == table.password:
                return render_template("dashboard.html")
    return render_template("login.html")


@app.route("/empdashboard")
def empdashboard():
    return render_template("empdashboard.html")


@app.route("/stafflogin", methods=['GET', 'POST'])
def stafflogin():
    if request.method == "POST":
        unam = request.form.get("username")
        passw = request.form.get("password")
        tables1 = Staff.query.filter_by()
        for table1 in tables1:
            if unam == table1.name and passw == table1.password:
                return render_template("empdashboard.html")
    return render_template("stafflogin.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/staffpatient")
def staffpatient():
    return render_template("staffpatient.html")


@app.route("/dashboard")
def dashboard():
    tables = Admin.query.filter_by().all()
    return render_template("dashboard.html", tables=tables)




@app.route("/employeemanagement")
def employeemanagement():
    return render_template("employeemanagement.html")


@app.route("/patientmanagement")
def patientmanagement():
    return render_template("patientmanagement.html")


@app.route('/profile')
def profile():
    return render_template('profile.html')


app.run(debug=True)

from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from form import VehiclePlateForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cars.db'
db = SQLAlchemy(app)
app.app_context().push()

class User(db.Model):
    Vehicle_Plate = db.Column(db.String(7), primary_key=True)
    Name = db.Column(db.String(20))
    Registration_number = db.Column(db.String(8))
    College = db.Column(db.String(20))
    Department = db.Column(db.String(20))
    Gender = db.Column(db.String(6))
    Email = db.Column(db.String(30))
    Phone = db.Column(db.String(15))

db.create_all()

nour = User(Vehicle_Plate="1234567", Name="Nour", Registration_number="12027771", College="IT", Department="CS", Gender="Male", Email="nour.ayyob@gmail.com", Phone="0595192015")
alice = User(Vehicle_Plate="9876543", Name="Alice", Registration_number="22334455", College="Engineering", Department="Mechanical", Gender="Female", Email="alice@example.com", Phone="1234567890")
bob = User(Vehicle_Plate="5432167", Name="Bob", Registration_number="33445566", College="Business", Department="Finance", Gender="Male", Email="bob@example.com", Phone="9876543210")
eva = User(Vehicle_Plate="7654321", Name="Eva", Registration_number="44556677", College="Arts", Department="History", Gender="Female", Email="eva@example.com", Phone="5556667777")

db.session.add(nour)
db.session.add(alice)
db.session.add(bob)
db.session.add(eva)

try:
    db.session.commit()
except Exception as e: 
    db.session.rollback()
finally:
    db.session.close()

@app.route("/", methods=['GET', 'POST'])
def home():
    form = VehiclePlateForm()
    if form.validate_on_submit():
        user = User.query.filter_by(Vehicle_Plate=form.VehiclePlate.data).first()
        if user is not None:
            return redirect(url_for('profile', userVehiclePlate=user.Vehicle_Plate))
    return render_template("home.htm", title_of_page="Home", css_file="home", form=form)

@app.route("/profile/<userVehiclePlate>")
def profile(userVehiclePlate):
    user = User.query.filter_by(Vehicle_Plate=userVehiclePlate).first()
    return render_template("profile.htm", title_of_page=user.Name, css_file="profile", User=user)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
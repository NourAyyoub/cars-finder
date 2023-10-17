from flask import Flask, render_template, redirect, url_for
from form import VehiclePlateForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

Users = [
    {"Name": "Nour Ayyoub", "Registration_number": "12027771", "College": "IT", "Department": "CS", "Gender": "Male", "Email": "nour.ayyob@gmail.com", "Phone": "0595192015", "Vehicle_Plate": "1234567"},
    {"Name": "Alice", "Registration_number": "22334455", "College": "Engineering", "Department": "Mechanical", "Gender": "Female", "Email": "alice@example.com", "Phone": "1234567890", "Vehicle_Plate": "9876543"},
    {"Name": "Bob", "Registration_number": "33445566", "College": "Business", "Department": "Finance", "Gender": "Male", "Email": "bob@example.com", "Phone": "9876543210", "Vehicle_Plate": "5432167"},
    {"Name": "Eva", "Registration_number": "44556677", "College": "Arts", "Department": "History", "Gender": "Female", "Email": "eva@example.com", "Phone": "5556667777", "Vehicle_Plate": "7654321"}
]

@app.route("/", methods=['GET', 'POST'])
def home():
    message = None
    form = VehiclePlateForm()
    if form.validate_on_submit():
        user = next((user for user in Users if user["Vehicle_Plate"] == form.VehiclePlate.data), None)
        if user is not None:
            return redirect(url_for('profile', username=user["Name"]))
        else:
            message = "User not found!"
    return render_template("home.htm", title_of_page="Home", css_file="home", form=form, message=message)

@app.route("/profile/<username>")
def profile(username):
    user = next((user for user in Users if user["Name"] == username), None)
    return render_template("profile.htm", title_of_page=user["Name"], css_file="profile", User=user)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
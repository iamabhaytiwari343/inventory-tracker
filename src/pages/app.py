from flask import Flask, render_template, request, redirect, session, url_for, flash
import pyrebase
import firebase_admin
from firebase_admin import credentials, auth

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Firebase Configuration
firebase_config = {
    "apiKey": "AIzaSyBPX4pFZ_Vj-82NgCwVTG1SOXAIwmFbue0",
    "authDomain": "inventorysoftware-d74dd.firebaseapp.com",
    "projectId": "inventorysoftware-d74dd",
    "storageBucket": "inventorysoftware-d74dd.firebasestorage.app",
    "messagingSenderId": "1024663209397",
    "appId": "1:1024663209397:web:7390fd6021232a66b245fc",
    "measurementId": "G-GQXHDZ6R63"
}

firebase = pyrebase.initialize_app(firebase_config)
auth_instance = firebase.auth()

# Firebase Admin SDK for verifying tokens
cred = credentials.Certificate("path/to/your/serviceAccountKey.json")
firebase_admin.initialize_app(cred)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        try:
            user = auth_instance.sign_in_with_email_and_password(email, password)
            session["user"] = user["idToken"]
            flash("Login successful!", "success")
            return redirect(url_for("dashboard"))
        except:
            flash("Invalid credentials. Please try again.", "danger")
    
    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        try:
            user = auth_instance.create_user_with_email_and_password(email, password)
            session["user"] = user["idToken"]
            flash("Signup successful! You can now log in.", "success")
            return redirect(url_for("login"))
        except:
            flash("Error creating account. Try again.", "danger")

    return render_template("signup.html")


@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return render_template("dashboard.html")
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("You have been logged out.", "info")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)

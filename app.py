from flask import Flask, request, render_template, redirect
from mysql.connector import Error, connect
import db_utils



app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    return render_template("welcome.html")


@app.route("/login", methods=["POST"])
def login():
    entered_email = request.form["username"]
    entered_password = request.form["password"]
    
    email_match_query = db_utils.mycursor.execute('''SELECT * FROM Users_Login WHERE user_email = %s AND user_password = %s''', [entered_email, entered_password])

    email_match_result = db_utils.mycursor.fetchone()

    
    if email_match_result:
        return "Login successful"
    else:
        return "The email and/or password you have entered are incorrect. Please try again."



if __name__ == "__main__":
    app.run(debug=True)
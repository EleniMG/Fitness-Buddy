from flask import Flask, request, render_template, redirect
from mysql.connector import Error, connect
import db_utils

app = Flask(__name__, template_folder="templates")

if __name__ == "__main__":
    app.run(debug=True)
# app.py
from flask import Flask
from models import db

app = Flask(__name__)

# Configure the database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the database with the app
db.init_app(app)

# Create a CLI command to create tables
@app.cli.command("create")
def create_tables():
    db.create_all()
    print("✅ Tables created!")

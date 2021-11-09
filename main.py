from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:hejsan123@localhost/testdatabasen'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databasen.db'
db = SQLAlchemy(app)

class Bil2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    namn = db.Column(db.String(80), unique=False, nullable=False)
    modell = db.Column(db.String(20), unique=False, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)


db.create_all()

while True:
    print("1. Skapa")
    print("2. Lista")
    sel = input("Val:")
    if sel == "1":
        b = Bil2()
        b.modell = input("Ange modell:")
        b.year = input("Ange year:")
        b.namn = input("Ange namn:")
        db.session.add(b)
        db.session.commit()
    if sel == "2":
        for m in Bil2.query.all():
            print(m.namn)



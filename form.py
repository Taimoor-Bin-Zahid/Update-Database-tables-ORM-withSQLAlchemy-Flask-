from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/sqlalchemy'
# app.config['SQLALCHEMY_MODIFICATIONS'] = True
db = SQLAlchemy(app)
class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False, nullable=False)
    gmail = db.Column(db.String, unique=True, nullable=False)

@app.route('/')
def index():
    fname="Taimoor"
    email="taimoor@gmail.com"
    entry = Contacts(name=fname, gmail=email)
    db.session.add(entry)
    db.session.commit()
    return "Success"

if __name__ == '__main__':
    app.run(debug=True)

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Event(db.Model):
    id = db.Column(db.Integer, db.Identity(start=0, cycle=True), primary_key=True, autoincrement=True)
    event = db.Column(db.String(80), nullable=False)
    date = db.Column(db.Date, nullable=False)

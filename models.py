from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)
    
class Animals(db.Model):
    
    __tablename__ = "pets"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False)


    
# - ***id***: auto-incrementing integer
# - ***name***: text, required
# - ***species***: text, required
# - ***photo_url***: text, optional
# - ***age***: integer, optional
# - ***notes***: text, optional
# - ***available***: true/false, required, should default to available
<<<<<<< HEAD
from database import db

class ContentOffering(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content_id = db.Column(db.Integer, db.ForeignKey('content_offering.id'), nullable=False)
    content = db.relationship('ContentOffering', backref=db.backref('cart_items', lazy=True))

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total_price = db.Column(db.Float, nullable=False)
=======
from database import db

class ContentOffering(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content_id = db.Column(db.Integer, db.ForeignKey('content_offering.id'), nullable=False)
    content = db.relationship('ContentOffering', backref=db.backref('cart_items', lazy=True))

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total_price = db.Column(db.Float, nullable=False)
>>>>>>> 89900e3c157d554cd02bbe13312b712e97820d9b

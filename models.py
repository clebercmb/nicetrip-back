from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class HouseAd(db.Model):
    __tablename__ = "HouseAds"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable = False)
    country = db.Column(db.String(50), nullable = False)
    address = db.Column(db.String(100), nullable = False)
    complement = db.Column(db.String(50), nullable = False)
    city = db.Column(db.String(50), nullable = False)
    state = db.Column(db.String(50), nullable = False)
    zipcode = db.Column(db.String(50), nullable = False)
    latitude = db.Column(db.Float, nullable = False)
    longitude = db.Column(db.Float, nullable = False)

    def __rep__(self):
        return "HouseAd %r>" % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "country": self.country,
            "address": self.address,
            "complement": self.complement,
            "city": self.city,
            "state": self.state,
            "zipcode": self.zipcode,
            "latitude": self.latitude,
            "longitude": self.longitude
        }
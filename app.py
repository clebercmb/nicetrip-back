import os 
from flask import Flask, request, jsonify, render_template
from flask_script import Manager 
from flask_migrate import Migrate, MigrateCommand
from models import db, HouseAd


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config["DEBUG"] = True
app.config["ENV"] = "development"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(BASE_DIR, "database.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

Migrate(app,db)

manager = Manager(app)
manager.add_command("db", MigrateCommand)

#Decorator that defines that above the function index() it is being aplied his route as "/"
@app.route("/")
def index():
    return render_template("home.html")
    
@app.route("/test")
def test():
    houseAd = HouseAd()

    houseAd.name="Casa Cidade"
    houseAd.country="Brazil"
    houseAd.address="Av Praia Grande"
    houseAd.complement= "Nothing"
    houseAd.city= "Santos"
    houseAd.state= "SP"
    houseAd.zipcode= "04200-000"
    houseAd.latitude = -23.998890
    houseAd.longitude = -46.413540
    

    db.session.add(houseAd)
    db.session.commit()

    return jsonify(houseAd.serialize()),201


@app.route("/houseads", methods=["GET", "POST"])
@app.route("/houseads/<int:id>", methods=["GET", "PUT", "DELETE"])
def contacts(id=None):
    if request.method == "GET":
        if id is not None:
            houseAd = HouseAd.query.get(id)
            if houseAd:
                return jsonify(houseAd.serialize()), 200
            else:
                return jsonify({"msg":"Contact not found"}), 404
        else:  
            houseAds = HouseAd.query.all()
            houseAds2 = list(map( lambda houseAd: houseAd.serialize(), houseAds ))
            return jsonify(houseAds2), 200

    if request.method == "POST":
        address = request.json.get("address", None)
        city = request.json.get("city", None)
        complement = request.json.get("complement", None)
        country = request.json.get("country", None)
        latitude = request.json.get("latitude", None)
        longitude = request.json.get("longitude", None)
        name = request.json.get("name", None)
        state = request.json.get("state", None)
        zipcode = request.json.get("zipcode", None)

        if not address:
            return jsonify({"msg":"name is required"}), 422

        if not city:
            return jsonify({"msg":"city is required"}), 422

        if not complement:
            return jsonify({"msg":"complement is required"}), 422

        if not country:
            return jsonify({"msg":"country is required"}), 422

        if not latitude:
            return jsonify({"msg":"latitude is required"}), 422

        if not longitude:
            return jsonify({"msg":"longitude is required"}), 422

        if not name:
            return jsonify({"msg":"name is required"}), 422   
            
        if not state:
            return jsonify({"msg":"state is required"}), 422   
                     
        if not zipcode:
            return jsonify({"msg":"zipcode is required"}), 422   

        houseAd = HouseAd()
        houseAd.name = name
        houseAd.country = country
        houseAd.address = address
        houseAd.complement = complement
        houseAd.city = city
        houseAd.state = state
        houseAd.zipcode = zipcode
        houseAd.latitude = latitude
        houseAd.longitude = longitude

        db.session.add(houseAd)
        db.session.commit()
        return jsonify(houseAd.serialize()),201

    if request.method == "PUT":
        address = request.json.get("address", None)
        city = request.json.get("city", None)
        complement = request.json.get("complement", None)
        country = request.json.get("country", None)
        latitude = request.json.get("latitude", None)
        longitude = request.json.get("longitude", None)
        name = request.json.get("name", None)
        state = request.json.get("state", None)
        zipcode = request.json.get("zipcode", None)

        
        if not address:
            return jsonify({"msg":"name is required"}), 422

        if not city:
            return jsonify({"msg":"city is required"}), 422

        if not complement:
            return jsonify({"msg":"complement is required"}), 422

        if not country:
            return jsonify({"msg":"country is required"}), 422

        if not latitude:
            return jsonify({"msg":"latitude is required"}), 422

        if not longitude:
            return jsonify({"msg":"longitude is required"}), 422

        if not name:
            return jsonify({"msg":"name is required"}), 422   
            
        if not state:
            return jsonify({"msg":"state is required"}), 422   
                     
        if not zipcode:
            return jsonify({"msg":"zipcode is required"}), 422 


        houseAd = HouseAd.query.get(id)

        if not houseAd:
            return jsonify({"msg":"Contact not found"}), 404


        houseAd.name = name
        houseAd.country = country
        houseAd.address = address
        houseAd.complement = complement
        houseAd.city = city
        houseAd.state = state
        houseAd.zipcode = zipcode
        houseAd.latitude = latitude
        houseAd.longitude = longitude

        db.session.commit()

        return jsonify(houseAd.serialize()),200

    if request.method == "DELETE":
        houseAd = HouseAd.query.get(id)

        if not houseAd:
            return jsonify({"msg":"Contact not found"}), 404


        db.session.delete(houseAd)
        db.session.commit()
        
        return jsonify(houseAd.serialize()),200

@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == "__main__":

    manager.run()

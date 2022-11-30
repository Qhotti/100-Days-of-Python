import random
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return "<a href='https://documenter.getpostman.com/view/24687196/2s8YszPWCZ' style=font-size:50px;>API_Docs</a>"
    
    



## HTTP GET - Read Record

@app.route("/random", methods=['GET'])
def random_cafe():
    cafes = Cafe.query.all()
    random_cafe = random.choice(cafes) 
    return jsonify(cafe=random_cafe.to_dict())

@app.route("/all", methods=['GET'])
def all_cafes():
    cafes = Cafe.query.all()
    return jsonify(cafes=[c.to_dict() for c in cafes])

@app.route("/search", methods=['GET'])
def search():
    ql = request.args.get("loc").title()
    cafe=db.session.query(Cafe).filter_by(location = ql)
    if [c.to_dict() for c in cafe] == []:
        return jsonify(error={'Not Found':'Sorry, we dont have a cafe at that location'}), 404
    else:
        return jsonify(cafe=[c.to_dict() for c in cafe])
    


## HTTP POST - Create Record

@app.route("/add", methods=['POST'])
def add():
    if request.method == "POST":



        new_cafe = Cafe(
        name = request.form.get("name"),
        map_url = request.form.get("map_url"),
        img_url = request.form.get("img_url"),
        location = request.form.get("location"),
        seats = request.form.get("seats"),
        has_toilet = bool(request.form.get("has_toilet")),
        has_wifi = bool(request.form.get("has_wifi")),
        has_sockets = bool(request.form.get("has_sockets")),
        can_take_calls = bool(request.form.get("can_take_calls")),
        coffee_price = request.form.get("coffee_price"))
        
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={'Success':'Successfully added the new cafe.'}), 200

## HTTP PUT/PATCH - Update Record

@app.route("/update-price/<int:cafe_id>", methods=['PATCH','GET'])
def update(cafe_id):
    new_price = request.args.get("new_price")
    
    try:
        cafe = db.session.query(Cafe).filter(Cafe.id == cafe_id).one()
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={'Success':'Successfully updated the price.'}), 200
    except:
        return jsonify(error={'Not Found':'Could not find a cafe with that id.'}), 404
        

## HTTP DELETE - Delete Record

@app.route("/report-closed/<cafe_id>", methods=['DELETE','GET'])
def delete(cafe_id):
    api_key = request.args.get("api-key")
    
    if api_key == 'TopSecretAPIKey':
        try:
            cafe = db.session.query(Cafe).filter(Cafe.id == cafe_id).one()
            if cafe:
                db.session.delete(cafe)
                db.session.commit()
                return jsonify(response={'Success':'Successfully deleted.'}), 200
        except:
            return jsonify(error={'Not Found':'Could not find a cafe with that id.'}), 404
    else:
        return jsonify(error={"invalid key":"Sorry, that's not allowed. Check your api_key."}),403
    

if __name__ == '__main__':
    app.run(debug=True)

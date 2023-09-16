from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import os
from pathlib import Path
app = Flask(__name__)
api = Api(app)
print(Path.cwd())
app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///" + os.path.join(Path.cwd(), "database.db")
db = SQLAlchemy(app)

#@app.before_first_request
#ef create_tables():
#    db.create_all()

class PersonModel(db.Model):
    id = db.Column(db.String(100), primary_key = True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.String(100), nullable=False)
    track = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Person(name:{name}, views:{age}, likes:{track})"

person_put_args = reqparse.RequestParser()
person_put_args.add_argument("user_id", type=str, help="ID of Person", required=True)
person_put_args.add_argument("name", type=str, help="name of Person", required=True)
person_put_args.add_argument("age", type=str, help="Age of Person", required=True)
person_put_args.add_argument("track", type=str, help="Track of Person", required=True)

person_update_args = reqparse.RequestParser()
person_update_args.add_argument("name", type=str, help="name of Person")
person_update_args.add_argument("age", type=str, help="age of Person")
person_update_args.add_argument("track", type=str, help="track of Person")

resource_fields = {
    "id": fields.String,
    "name": fields.String,
    "age": fields.String,
    "track": fields.String
}

class CreatePerson(Resource):
    @marshal_with(resource_fields)
    def put(self):
        args = person_put_args.parse_args()
        result = PersonModel.query.filter_by(id=args["user_id"]).first()
        if result:
            abort(409, message="User ID already exists")
        user = PersonModel(id=args["user_id"], name=args["name"], age=args["age"], track=args["track"])
        db.session.add(user)
        db.session.commit()
        return user, 201


class Person(Resource):
    @marshal_with(resource_fields)
    def get(self,user_id):
        result = PersonModel.query.filter_by(id=user_id).first()
        if not result:
            abort(404, message= "could not find user with that ID")
        return  result

    @marshal_with(resource_fields)
    def patch(self, user_id):
        args =person_update_args.parse_args()
        result = PersonModel.query.filter_by(id=user_id).first()
        if not result:
            abort(404, message="User ID doesn't exists")

        if args["name"]:
            result.name=  args["name"]
        if args["age"]:
            result.age=  args["age"]
        if args["track"]:
            result.track=  args["track"]

        db.session.commit()
        return result, 200

    @marshal_with(resource_fields)    
    def delete(self, user_id):
        result = PersonModel.query.filter_by(id=user_id).first()
        if not result:
            abort(404, message="User ID doesn't exists")

        db.session.delete(result)
        db.session.commit()
        return result




api.add_resource(Person, "/api/<string:user_id>")
api.add_resource(CreatePerson, "/api")
if __name__ == "__main__":
    app.run(debug=True)
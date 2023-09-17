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

@app.before_first_request
def create_tables():
    db.create_all()

class PersonModel(db.Model):
    name = db.Column(db.String(100),primary_key = True, nullable=False)
    
    def __repr__(self):
        return f"Person(name:{name})"

person_put_args = reqparse.RequestParser()
person_put_args.add_argument("name", type=str, help="name of Person", required=True)

person_update_args = reqparse.RequestParser()
person_update_args.add_argument("name", type=str, help="name of Person")

resource_fields = {
    "name": fields.String
}

class CreatePerson(Resource):
    @marshal_with(resource_fields)
    def put(self):
        args = person_put_args.parse_args()
        result = PersonModel.query.filter_by(name=args["name"]).first()
        if result:
            abort(409, message="User ID already exists")
        user = PersonModel(name=args["name"])
        db.session.add(user)
        db.session.commit()
        return user, 201


class Person(Resource):
    @marshal_with(resource_fields)
    def get(self,user_id):
        result = PersonModel.query.filter_by(name=user_id).first()
        if not result:
            abort(404, message= "could not find user with that ID")
        return  result

    @marshal_with(resource_fields)
    def patch(self, user_id):
        args =person_update_args.parse_args()
        result = PersonModel.query.filter_by(name=user_id).first()
        if not result:
            abort(404, message="User ID doesn't exists")

        if args["name"]:
            result.name=  args["name"]
        
        db.session.commit()
        return result, 200

    @marshal_with(resource_fields)    
    def delete(self, user_id):
        result = PersonModel.query.filter_by(name=user_id).first()
        if not result:
            abort(404, message="User ID doesn't exists")

        db.session.delete(result)
        db.session.commit()
        return result




api.add_resource(Person, "/api/<string:user_id>")
api.add_resource(CreatePerson, "/api")
if __name__ == "__main__":
    app.run(debug=True)
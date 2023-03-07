from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

if __name__ == '__main__':
    pass
    #app.run(debug=True)


app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5434/flask_react"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class SchoolModel(db.Model):
    __tablename__ = 'schools'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    address = db.Column(db.String())
    summary = db.Column(db.String())

    def __init__(self, name, address, summary):
        self.name = name
        self.address = address
        self.summary = summary

    def __repr__(self):
        return f"<School {self.name}>"

@app.route("/")
def index():
    return "React App Demo"


@app.route("/api/school/all", methods=['GET'])
def getSchools():
    if request.method == 'GET':
        schools = SchoolModel.query.all()
        results = [
            {
                "name": school.name,
                "address": school.address,
                "summary": school.summary
            } for school in schools]

        return {"count": len(results), "schools": results}

@app.route("/api/school/create", methods=['POST'])
def postSchool():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_item = SchoolModel(name=data['name'], address=data['address'], summary=data['summary'])
            db.session.add(new_item)
            db.session.commit()
            return {"message": f"entry {new_item.name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}
    else:
        return

@app.route("/members")
def members():
    return {"data":[{"name":"User1"}, {"name":"User2"}, {"name":"User3"}]}

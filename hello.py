from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Creating a database using SQLAchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///example.db"

db =SQLAlchemy(app)

class First_row(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(50), nullable=False)
    destination = db.Column(db.String(50), nullable=False)
    somethingElse = db.Column(db.Float, nullable=False)

    # converts the json into a python dict
    def to_dict(self):
        return {
            "id": self.id,
            "source": self.source,
            "destination": self.destination,
            "somethingElse": self.somethingElse
        }




with app.app_context():
    db.create_all()



@app.route('/')
def home():
    return jsonify({"message": "This is the home page!"})

@app.get('/api/hello')
def hello():
    return {
        "message": "Hello!"
    }

@app.get('/api/user/<int:user_id>')
def get_user(user_id):
    return {
        "user_id": user_id
    }

@app.post('/api/user')
def create_user():

    data = request.get_json()

    return {
        "message": "User created",
        "user": data
    }, 201


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAchemy

app = Flask(__name__)

# Creating a database using SQLAchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///example.db"

db =SQLAchemy(app)

class First_row(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column()
    destination = db.Column()
    somethingElse = db.Column()

    # converts the json into a python dict
    def to_dict(self):
        return {
            "id": self.id,
            "source": self.source,
            "destination": self.destination,
            "somethingElse": self.somethingElse
        }







@app.route('/')
def home():
    return {"message": "This is the home page!"}

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

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import json
app = Flask(__name__)
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    language = db.Column(db.String(50))

@app.route('/add_info', methods=['POST'])
def add_info():
    info_data = request.get_json()

    new_info = Info(name=info_data['name'], age=info_data['age'], language=info_data['language'])

    db.session.add(new_info)
    db.session.commit()

    return 'Done', 201

@app.route('/info')
def info():
    info_list = Info.query.all()
    infos = []

    for info in info_list: 
        infos.append({'name': info.name, 'age' : info.age, 'language' : info.language})

    response = jsonify({'info': infos})
    return response


if __name__ == "__main__":
    app.run(debug=True)

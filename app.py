from flask import Flask, render_template, request
import yaml
from yaml import Loader
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

coords = []


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)


def routeFinder(coords):
    return coords


@app.route('/')
def hello_world():  # put application's code here
    with open('config.yaml') as f:
        config = yaml.load(f, Loader=Loader)
    print(config)
    routeFinder(coords)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

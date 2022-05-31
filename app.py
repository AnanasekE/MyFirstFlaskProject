from flask import Flask, render_template, request
import yaml
from yaml import Loader

app = Flask(__name__)


def routeFinder():
    return 'SUS'


@app.route('/')
def hello_world():  # put application's code here
    with open('config.yaml') as f:
        config = yaml.load(f, Loader=Loader)
    print(config)

    return render_template('index.html')


if __name__ == '__main__':
    app.run()

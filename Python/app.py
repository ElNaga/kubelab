from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    print(requset.json)
    # da vidis od body kako se zema info vo flaskj
    return "<p>Hello, World!</p>"c
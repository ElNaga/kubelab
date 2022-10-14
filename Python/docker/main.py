"""test Flask with this"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World! Hello Kubelab! From docker build.. wow'

if __name__ == "__main__":
    app.run(debug=True)

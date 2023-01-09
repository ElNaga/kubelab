from flask import Flask, request
import requests
import json
import hashlib
import jwt
import handlers.token as t



app = Flask(__name__)


@app.route('/', methods=['POST'])
def api():
    # funk za zapishuvanje vo baza
    return t.token(request.get_json())


if __name__ == '__main__':
    app.run(port=5000)

import jwt
import tokenize


def token(data):
    
    encoded_jwt = jwt.encode(data, "tajna", algorithm="HS256")
    print(encoded_jwt)

    return encoded_jwt
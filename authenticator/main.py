from flask import Flask, request, Response
import jwt
from datetime import timedelta, datetime
<<<<<<< HEAD
import os
import sys

=======
>>>>>>> 40d6d45f9128e9a1be8629d57efbb1459a6d1a9c
app = Flask(__name__)

users = [
    {'username': 'david', 'password': 'mypassword'},
    {'username': 'eve', 'password': 'mypassword2'},
    {'username': 'caio', 'password': 'mypassword3'},
]

@app.route("/authenticate", methods = ['POST'])
def authenticate():
    try:
        body = request.get_json()
        username = body['username']
        password = body['password']
        # Check if the user is authorized:
        for user in users:
            if user['username'] == username and user['password'] == password:
                # Authentication succeeded
                claims = {
                    "iss": "cct",
                    "sub": username,
                    "aud": "users",
                    "exp": (datetime.now() + timedelta(minutes = 5)).timestamp(),
                    "iat": datetime.now().timestamp(),
                    "role": "user"
                }
<<<<<<< HEAD
                return {'token': jwt.encode(claims, os.environ.get("JWT_SECRET"), algorithm="HS256")}                
=======
                return {'token': jwt.encode(claims, "this-is-a-secret", algorithm="HS256")}                
>>>>>>> 40d6d45f9128e9a1be8629d57efbb1459a6d1a9c
    except:
        return Response('Unauthorized', 401)
    return Response('Unauthorized', 401)

if __name__ == '__main__':
<<<<<<< HEAD
    if not os.environ.get("JWT_SECRET"):
        print("JWT secret (JWT_SECRET) environment variable missing")
        sys.exit(-1)

    app.run(port=5001, host='0.0.0.0')
=======
    app.run()
>>>>>>> 40d6d45f9128e9a1be8629d57efbb1459a6d1a9c

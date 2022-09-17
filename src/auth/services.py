import jwt
from datetime import datetime, timezone, timedelta
from core.config import SECRET_KEY
from src.users.models import Users


def login(credentials):
    _email = credentials.get("email")
    _password = credentials.get("password")

    user_exists = Users.query.filter_by(email=_email).first()

    if not user_exists:
        return {"msg": "This email does not exist."}, 400

    if not user_exists.check_password(_password):
        return {"msg": "Wrong credentials."}, 400

    # create access token uwing JWT
    token = jwt.encode({'email': _email, 'exp': datetime.utcnow() + timedelta(minutes=30)}, SECRET_KEY)

    user_exists.set_jwt_auth_active(True)
    user_exists.save()

    return {
            "msg": "Logged in successfully.",
            "token": token,
            "data": user_exists.toJSON()}, 200


def register(data):
    _email = data.get("email")
    _password = data.get("password")

    user_exists = Users.query.filter_by(email=_email).first()
    if user_exists:
        return {"msg": "Email already taken"}, 400

    new_user = Users(email=_email)

    new_user.set_password(_password)
    new_user.save()

    return {
            "msg": "The user was successfully registered",
            "data": {
                "userID": new_user.id
                }}, 200
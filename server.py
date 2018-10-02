from flask import Flask, request, Response
import RPi.GPIO as GPIO
from garage_door import GarageDoor
from config import Config

app = Flask(__name__)
garage_door_opener = GarageDoor(GPIO)
config = Config()


def open_door(door):
    if door == "left":
        garage_door_opener.toggle_left_door()
    elif door == "right":
        garage_door_opener.toggle_right_door()
    elif door == "other":
        garage_door_opener.toggle_other_door()


@app.route("/garage/toggle", methods=["POST"])
def toggle_door():
    print("Got request.")
    if request.headers.get("AuthKey") == config.auth_key():
        door = request.json["door"]
        print("opening door: " + door)
        open_door(door)
        return Response("triggered!", 200)
    return Response("Not Authorized", 401)


app.run(host="0.0.0.0", port=config.port())

from flask import Flask, request
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
    if request.headers.get("AuthKey") == config.auth_key():
        door = request.json["door"]
        open_door(door)


app.run(port=config.port())

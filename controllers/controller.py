from flask import render_template, request, redirect
from app import app
from models.event_list import events, add_new_event
from models.event import Event

@app.route("/")
def index():
    return render_template("index.html", title="Home", events = events)

@app.route("/<event_index>")
def event(event_index):
    event_to_return = events[int(event_index)]
    return render_template("event.html", title="Event Information", event= event_to_return)


@app.route("/", methods=["POST"])
def add_event():
    event_date = request.form["event_date"]
    event_name = request.form["event_name"]
    num_of_guests = request.form["num_of_guests"]
    room_location = request.form["room_location"]
    event_description = request.form["event_description"]
    recurring = False
    if request.form["recurring"] == "On":
        recurring = True
    
    
    new_event= Event(event_date, event_name, num_of_guests, room_location, event_description, recurring)
    add_new_event(new_event)
    return redirect("/")


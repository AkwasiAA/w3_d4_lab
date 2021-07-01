class Event:
    def __init__(self, date, event_name, num_of_guests, room_location, event_description, recurring):
        self.date = date
        self.event_name = event_name
        self.num_of_guests = num_of_guests
        self.room_location = room_location
        self.event_description = event_description
        self.recurring = recurring
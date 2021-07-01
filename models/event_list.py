from models.event import Event

event_1 = Event("14/10/2021", "CodeClan Graduation", 19, "CodeClan HQ", "The graduation of Cohort E50 PSD", False)
event_2 = Event("01/01/2021", "New Year's Day", 343, "Princes Street", "The 'world famous' street party", True)
event_3 = Event("31/03/2021", "St. Patrick's Day", 600, "Finnegans Wake", "Dublin City Centre", True)

events = [event_1, event_2, event_3]

def add_new_event(event_to_add):
    events.append(event_to_add)
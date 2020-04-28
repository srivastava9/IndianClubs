# Script File for Populating Database into sqlite using django
# written by Aditya Srivastava
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IndianClubs.settings')

import django
django.setup()
import json


from Club.models import State, Club

states = []
try:
    with open('football-database.json', 'r') as file:
        data = json.load(file)
except Exception as exc:
    print("Some Error: %s" % (exc))

for key, value in data.items():
    states.append(key)
# print(states)


def populate_database(states, data):
    def add_state(name):
        s = State.objects.get_or_create(name=name)[0]
        s.save()
        return s

    def add_clubs(each_data, state_name):
        c = Club.objects.get_or_create(Name=each_data["Name"],
                                       State=State.objects.get_or_create(
                                           name=state_name)[0],
                                       League=each_data["League"],
                                       City=each_data["City"])[0]

        c.save()
        return c

    for state in states:
        add_state(state)

    for key, value in data.items():
        for each in value:
            add_clubs(each, key)

print("Starting population script...")
populate_database(states,data)
print("Done !")

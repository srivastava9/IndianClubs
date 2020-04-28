# Script File for Scraping wikipedia Data and converting to JSON
# written by Aditya Srivastava
import requests
from bs4 import BeautifulSoup
import json
URL = "https://en.wikipedia.org/wiki/List_of_football_clubs_in_India"
page = requests.get(URL)
try:
    page.raise_for_status()
except Exception as exc:
    print("the page could not be found Error: %s" % (exc))

soup = BeautifulSoup(page.content, 'html.parser')
data = {}
states = []
# function for creating state data


def get_states():
    results = soup.find(id="mw-content-text")
    # print(results.prettify())

    states_html = results.find_all('h3')
    for state_html in states_html:
        states.append(state_html.find("span", "mw-headline"))
    return None

# adding data of club,city and league to each state


def add_clubs_data(states, data):
    for state in states:
        table_html = state.find_next("table")
        rows = table_html.find("tbody").find_all("tr")
        club_data = []
        for row in rows[1:]:

            row_data = row.find_all("td")
            try:
                club_data.append({"Name": row_data[0].text.strip(),
                                  "City": row_data[1].text.strip(), "League": row_data[2].text.strip()})
            except IndexError:
                club_data.append(
                    {"Name": row_data[0].text.strip(), "City": "-", "League": "-"})
            data[state.text.strip()] = club_data
    return None


get_states()
add_clubs_data(states, data)
try:
    with open('football-database.json', 'w') as file:
        json.dump(data, file)
    print("It worked!")
except Exception as exc:
    print("Some Error : %s" % (exc))
# print(data)

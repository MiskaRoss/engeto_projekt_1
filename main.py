"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Michaela Rossmannová
email: rossmannova.m@gmail.com
discord: misa02907
"""

import csv
import sys
import requests
from bs4 import BeautifulSoup


# Odkaz pro stahování:
def get_url():
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


# Ověření správně zadaných argumentů:
def check_arguments():
    if len(sys.argv) != 3:
        print("Program need 2 arguments, I'm exiting the program")
        exit()
    elif not base_url.startswith("https://www.volby.cz/pls/ps2017nss/"):
        print("Wrong url, I'm exiting the program")
        exit()
    elif not file_name.endswith(".csv"):
        print("Must be .csv file, I'm exiting the program")
        exit()


# získá číselné označení obcí
def get_town_numbers():
    town_numbers = []
    code_elements = get_url().find_all("td", "cislo")
    for code in code_elements:
        town_numbers.append(code.get_text())
    return town_numbers


# Získá názvy obcí
def get_town_names():
    town_names = []
    code_elements = get_url().find_all("td", "overflow_name")
    for code in code_elements:
        town_names.append(code.get_text())
    return town_names


# vytvoří list s jednotlivými url obcí
def get_codes_url():
    url_list = []
    url_towns = get_url().find_all("td", "cislo")

    for url in url_towns:
        url_list.append(url.find("a")["href"])
    sub_url = ["https://volby.cz/pls/ps2017nss/" + url_list[i] for i in range(len(url_list))]
    return sub_url


# získá informace z url jednotlivými obcí
def sub_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


# získá počet voličů v seznamu
def get_registered():
    register_list = []
    cities = get_codes_url()
    for url in cities:
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'html.parser')
        voters = soup.find_all("td", "cislo", headers="sa2")
        for voter in voters:
            register_list.append(voter.text)
    return register_list


# vydané obálky:
def get_envelopes():
    envelope_list = []
    cities = get_codes_url()
    for url in cities:
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'html.parser')
        envelopes_elements = soup.find_all("td", "cislo", headers="sa2")
        for envelope in envelopes_elements:
            envelope_list.append(envelope.text)
    return envelope_list


# získá počet platných hlasů
def get_valid_votes() -> list:
    validate_list = []
    cities = get_codes_url()
    for url in cities:
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'html.parser')
        validate_elements = soup.find_all("td", "cislo", headers="sa6")
        for validate in validate_elements:
            validate_list.append(validate.text)
    return validate_list


# získá první url s obcí
def sub_url_partis():
    response = requests.get(get_codes_url()[0])
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


# získá názvy všech stran
def get_party():
    parties = []
    cities = get_codes_url()
    for url in cities:
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'html.parser')
        party_elements = soup.find_all("td", "overflow_name")
        for party in party_elements:
            parties.append(party.text)
    return parties


# vytvoří list se všemi hlasy v dané obci
def get_votes():
    votes_list = []
    cities = get_codes_url()
    for url in cities:
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'html.parser')
        votes_elements = soup.find_all("td", "cislo", headers=["t1sb3", "t2sb3"])
        for vote in votes_elements:
            votes_list.append(vote.text)
    return votes_list


# vytvoří se soubor dle druhého zadaného argumentu a vypíše se tabulka řádek po řádku
def csv_output(link, name_of_file):
    print("Downloading...")
    header = ["code", "location", "registered", "envelopes", "valid"] + get_party()

    rows = [header]
    town_codes = get_town_numbers()
    town_names = get_town_names()
    registered = get_registered()
    envelopes = get_envelopes()
    valid_votes = get_valid_votes()
    party_votes = get_votes()

    for i in range(len(town_names)):
        row = [town_codes[i], 
               town_names[i],
               registered[i],
               envelopes[i],
               valid_votes[i]
        ] + party_votes[i*len(get_party()): (i+1)*len(get_party())]
        rows.append(row)

    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print(f"Download complete. Saved file: {file_name}")


if __name__ == "__main__":
    base_url = 'https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=6&xnumnuts=4205'
    file_name = 'vysledky_most.csv'
    csv_output(base_url, file_name)

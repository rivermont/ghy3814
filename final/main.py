#!/usr/bin/env python3

import requests
import csv
import json

overwrite = False  # for overwriting data files

if overwrite:
    # get data from usda csvs
    commercial = requests.get("https://www.aphis.usda.gov/animal_health/data-csv/hpai-commercial-backyard-flocks.csv").text
    wild = requests.get("https://www.aphis.usda.gov/animal_health/data-csv/hpai-wild-birds.csv").text
    # https://www.aphis.usda.gov/animal_health/data-csv/hpai-commercial-backyard-flocks.csv
    # https://www.aphis.usda.gov/animal_health/data-csv/hpai-wild-birds.csv

    # check whether files exist
    # save files
    with open("./hpai-commercial-backyard-flocks.csv", "w+") as f:
        f.write(commercial)

    with open("hpai-wild-birds.csv", "w+") as f:
        f.write(wild)


# ['State', 'County', 'Date Confirmed', 'Flock Type', 'Flock Size']
data = {}

with open("./hpai-commercial-backyard-flocks.csv", "r") as f:
    creader = csv.reader(f, delimiter=',', quotechar='"')
    header = next(creader)
    
    for row in creader:
        state = row[0]
        county = row[1]
        ftype = row[3]
        fsize = row[4]
        
        if state not in data:
            data[state] = {'counties': {}, 'num_birds_cap': 0, 'num_report_cap': 0}
        
        if county not in data[state]['counties']:
            data[state]['counties'][county] = {'description': '', 'num_birds_cap': 0, 'num_report_cap': 0}
        
        data[state]['counties'][county]['description'] += ftype + ': ' + fsize + '\n'
        data[state]['counties'][county]['num_birds_cap'] += int(fsize.replace(',', ''))
        data[state]['counties'][county]['num_report_cap'] += 1
        data[state]['num_birds_cap'] += int(fsize.replace(',', ''))  # can also automate this at the end
        data[state]['num_report_cap'] += 1

x = set()
for s in data:
    for c in data[s]['counties']:
        x.add((s, c))


with open("./cb_2020_us_county_20m.geojson", 'r') as f:
    counties = json.loads(f.read())
    for county in counties['features']:
        if (county['properties']['STATE_NAME'], county['properties']['NAME']) in x:
            print(county['properties']['NAME'])
            # add counties[county] to output


# parse csvs, reading into dict:
# {state: {counties: {county1: {...}, ...}, num_birds_wild: 0, num_report_wild: 0, num_birds_cap: 0, num_report_cap: 0}, ...}

# For state in geojson, if state in list, add to file
# for county in geojson, if state and county in list, add to file

# print final geojson(s)?


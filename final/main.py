#!/usr/bin/env python3

import requests

# get data from usda csvs
# https://www.aphis.usda.gov/animal_health/data-csv/hpai-commercial-backyard-flocks.csv
# https://www.aphis.usda.gov/animal_health/data-csv/hpai-wild-birds.csv

# parse csvs, reading into dict:
# {state: {counties: {county1: {...}, ...}, num_birds_wild: 0, num_report_wild: 0, num_birds_cap: 0, num_report_cap: 0}, ...}

# for each state, add state geojson to file
# for each state: for each county, add county geojson to file

# print final geojson(s)?


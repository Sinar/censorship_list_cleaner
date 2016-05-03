import csv_dict
import requests
from requests.exceptions import *
import argparse

def check_valid(list_path):
    datas = csv_dict.csv_dict(list_path)
    for data in datas:
        try:
            r = requests.get(data["url"])
            if r.status_code != 200:
                print(data["url"], str(r.status_code))
        except ConnectionError:
            print(data["url"], "connection_error")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="list_checker")
    parser.add_argument("list_path", help="path of the citizenlab csv for country", action="store")
    param = parser.parse_args()

    check_valid(param.list_path)

#!/usr/bin/env python3

import os
import sys
import json
import requests
import argparse


def make_request(mac_address):
    params = {
        "apiKey" : os.environ['API_KEY'],
        "output" : 'json',
        "search" : mac_address
    }

    response = requests.get(url=os.environ['API_ADDRESS'], params=params)

    if response.status_code != 200:
        print("API returned HTTP {}".format(response.status_code), file=sys.stderr)
        return False
    else:
        return json.loads(response.text)


def get_company_name(mac_info_dict):
    return mac_info_dict['vendorDetails']['companyName']




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mac", help="a mac address to do a search on")
    args = parser.parse_args()
    
    mac_info = make_request(args.mac)
    if not mac_info:
        sys.exit(1)
    else:
        print(get_company_name(mac_info))
        sys.exit(0)

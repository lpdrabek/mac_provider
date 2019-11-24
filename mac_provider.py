#!/usr/bin/env python3

import argparse


def prepare_mac(mac_address):
    parsed_mac = mac_address.replace(":", "")
    parsed_mac = parsed_mac.replace("-", "")
    parsed_mac = parsed_mac.replace(".", "")

    return parsed_mac




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mac", help="a mac address to do a search on")
    args = parser.parse_args()

    print(prepare_mac(args.mac))
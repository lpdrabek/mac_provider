#!/usr/bin/env python3

import sys

def prepare_mac(mac_address):
    parsed_mac = mac_address.replace(":", "")
    parsed_mac = parsed_mac.replace("-", "")
    parsed_mac = parsed_mac.replace(".", "")

    return parsed_mac


if __name__ == "__main__":
    print(prepare_mac(sys.argv[1]))
#!/usr/bin/env python3

mac = "44:38:39:ff:ef:57"

def prepare_mac(mac_address):
    parsed_mac = mac_address.replace(":", "")
    parsed_mac = parsed_mac.replace("-", "")
    parsed_mac = parsed_mac.replace(".", "")

    return parsed_mac


print(prepare_mac(mac))
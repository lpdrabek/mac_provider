import os
import json
import requests
import responses

import mac_provider

mac = "443839ffef57"
company_name = "Cumulus Networks, Inc"

API_MOCK='https://api.macaddress.io/v1?apiKey={}&output=json&search={}'.format(os.environ['API_KEY'], mac)
API_RESPONSE='{"vendorDetails":{"oui":"443839","isPrivate":false,"companyName":"Cumulus Networks, Inc","companyAddress":"650 Castro Street, suite 120-245 Mountain View CA 94041 US","countryCode":"US"},"blockDetails":{"blockFound":true,"borderLeft":"443839000000","borderRight":"443839FFFFFF","blockSize":16777216,"assignmentBlockSize":"MA-L","dateCreated":"2012-04-08","dateUpdated":"2015-09-27"},"macAddressDetails":{"searchTerm":"443839ffef57","isValid":true,"virtualMachine":"Not detected","applications":["Multi-Chassis Link Aggregation (Cumulus Linux)"],"transmissionType":"unicast","administrationType":"UAA","wiresharkNotes":"No details","comment":""}}'


@responses.activate
def test_make_request():
    responses.add(responses.GET, API_MOCK, json=json.loads(API_RESPONSE), status=200)
    resp = mac_provider.make_request(mac)

    assert resp == json.loads(API_RESPONSE)


@responses.activate
def test_make_request_bad():
    responses.add(responses.GET, API_MOCK, json=json.loads(API_RESPONSE), status=500)
    resp = mac_provider.make_request(mac)

    assert resp == False

def test_get_company_name():
    assert company_name == mac_provider.get_company_name(json.loads(API_RESPONSE))
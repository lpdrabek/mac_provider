# mac_provider

A Python3 script retrieving company name from a MAC address by accessing [macaddress.io](https://macaddress.io/ "macaddress.io") API.

## How to run it
### Docker
1. Copy `Dockerfile.template` as `Dockerfile` - `cp Dockerfile.template Dockerfile`
2. Replace `ENTER_YOUR_KEY_HERE` with your API key from macaddress.io in `Dockerfile`
3. Build your image `docker build -t mac_provider .`
4. Run the  script with `docker run mac_provider MAC_ADDRESS` replacing MAC_ADDRESS with actual value

### Standalone script
This script uses environment variables to determine api address and api key, before running it from the command line run
```bash 
export API_ADDRESS=https://api.macaddress.io/v1
export API_KEY=YOUR_KEY_OBTAINED_FROM_MACADDRESS.IO
```

then install requirements by running 
`pip install -r requirements.txt`

Run the code with 
`python3 mac_provider.py MAC_ADDRESS`

## How to test it
1. Run `pip install -r requirements-dev.txt`
2. Run `pytest` in repository root directory
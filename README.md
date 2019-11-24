# mac_provider

A Python3 script retrieving company name from a MAC address by accessing [macaddress.io](https://macaddress.io/ "macaddress.io") API.

## How to run it
### Docker
1. Replace `ENTER_YOUR_KEY_HERE` with your API key from macaddress.io
2. Rename `Dockerfile.template` to `Dockerfile` - `mv Dockerfile.template Dockerfile`
3. Build your image `docker build .`
4. Run the  script with `docker run IMAGE_CODE MAC_ADDRESS` replacing IMAGE_CODE and MAC_ADDRESS with actual values

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


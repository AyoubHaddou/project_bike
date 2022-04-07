import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here 
data = {
  "Inputs": {
    "data": [
      {
        "Column2": "onsenfou",
        "season": 0,
        "holiday": 0,
        "workingday": 0,
        "weather": 1,
        "temp": -1.0,
        "atemp": 0.0,
        "humidity": 0,
        "windspeed": 0.0,
        "day": 0,
        "hour": 0,
        "year": 0
      },
      {
        "Column2": "onsenfou",
        "season": 0,
        "holiday": 0,
        "workingday": 0,
        "weather": 2,
        "temp": 0.0,
        "atemp": 0.0,
        "humidity": 15,
        "windspeed": 0.0,
        "day": 0,
        "hour": 0,
        "year": 0
      }
    ]
  },
  "GlobalParameters": 0.0
}

body = str.encode(json.dumps(data))

url = 'http://871c041d-2e05-4f25-9aa3-f5b57f00516f.westeurope.azurecontainer.io/score'
api_key = '' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))

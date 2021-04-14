import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

data = {
    "data":
    [
        {
            "age": 75,
            "anaemia": 0,
            "creatinine_phosphokinase": 582,
            "diabetes": 0,
            "ejection_fraction": 20,
            "high_blood_pressure": 1,
            "platelets": 265000,
            "serum_creatinine": 1.9,
            "serum_sodium": 130,
            "sex": 1,
            "smoking": 0,
            "time": 4,
        },
    ],
}

body = str.encode(json.dumps(data))

url = 'http://23f71748-edf8-4269-97cb-f8df0fc734f3.southcentralus.azurecontainer.io/score'
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
    print(json.loads(error.read().decode("utf8", 'ignore')))
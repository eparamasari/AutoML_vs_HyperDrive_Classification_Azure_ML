import requests
import json

scoring_uri = 'http://23f71748-edf8-4269-97cb-f8df0fc734f3.southcentralus.azurecontainer.io/score'
# If the service is authenticated, set the key or token
key = ''

# Two sets of data to score, so we get two results back
data = {"data":
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
            "time": 4
          },
          {
            "age": 49,
            "anaemia": 1,
            "creatinine_phosphokinase": 80,
            "diabetes": 0,
            "ejection_fraction": 30,
            "high_blood_pressure": 1,
            "platelets": 427000,
            "serum_creatinine": 1,
            "serum_sodium": 138,
            "sex": 0,
            "smoking": 0,
            "time": 12
          },
      ]
    }
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {key}'

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())



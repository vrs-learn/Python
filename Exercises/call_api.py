import requests
import json

api_url = 'http://clm-aus-018787:38080/baocdp/rest/login'

#header = { "Content-Type" : "application/json", "username" : "aoadmin", "password" : "admin123"}
header = {"username" : "aoadmin", "password" : "admin123"}

r = requests.post(api_url, json=header)

auth_token = r.headers['Authentication-Token']

print(auth_token)

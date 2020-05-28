import requests
import json

def fortune():
    url = "http://yerkee.com/api/fortune/all"

    response = requests.request("GET",url)
    data = response.json()
    return data['fortune']    

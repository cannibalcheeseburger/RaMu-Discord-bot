import requests
import json

def shake(query):
    url = "https://shakespeare.p.rapidapi.com/shakespeare.json"

    querystring = {"text":query}

    headers = {
        'x-rapidapi-host': "shakespeare.p.rapidapi.com",
        'x-rapidapi-key': "824bc0944dmsha1058bd1b0cc53ap1e9c21jsnb8d7f51fef9e",
        'x-funtranslations-api-secret': ""
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    if data['error']:
        return(data['error']['message'])
    return(data['contents']['translated'])
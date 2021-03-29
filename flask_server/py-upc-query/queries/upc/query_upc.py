import requests

base_url = "https://barcode-monster.p.rapidapi.com/"

def query(upc):
    url = base_url + upc

    headers = {
        'x-rapidapi-key': "e1bb5504e0msh24ce22449b9b84dp14fd85jsna238fb4f77ec",
        'x-rapidapi-host': "barcode-monster.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers).json()

    __clean_desc(response)

    print('upc query done')

    return response

def __clean_desc(json_dict):
    json_dict["description"] = json_dict["description"][:-23]

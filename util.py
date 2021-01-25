from random import randint
import requests
from credentials import username, password

def create_meme_api_request(input_str):
    template_id = 102156234	
    URL = 'https://api.imgflip.com/caption_image'
    usr = username
    pw = password
    params = {
    'username':usr,
    'password':pw,
    'template_id':template_id,
    'boxes[0][text]':input_str
    }
    response = requests.request('POST',URL,params=params).json()
    return response['data']['url']

def generate_spongebobify_text(input_str):
    text = input_str
    result = ""
    for i in text:
        case = randint(1,2)
        if case == 1:
            i = i.lower()
        else:
            i = i.upper()
        result += i
    return result
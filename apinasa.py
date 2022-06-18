import requests
import json
from datetime import datetime


API_KEY =''

API_URL = 'https://api.nasa.gov/planetary/apod?api_key=GKnVjFnA6ibq3RZHdZjBELU82co13qDkkveoSpyM'

#DATE = '2020-01-01'
DATE = datetime.today().strftime('%Y-%m-%d')

params = {
    'api_key': API_KEY,
    'hd': 'True',
    'date': DATE
}

response = requests.get(API_URL, params=params)
json_data = json.loads(response.text)
image_url = json_data['url']
image_title = json_data['title']
image_explanation = json_data['explanation']
#image_hdurl = json_data['hdurl']
image_types = json_data['media_type']

def imageurl(): 
    return image_url

def imagetitle(): 
    return image_title
    
def imageexplanation(): 
   return image_explanation

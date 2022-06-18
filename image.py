import requests

def image_download(link):
    f = open('day.jpg','wb')
    response = requests.get(link)
    f.write(response.content)
    f.close()
    return print("download successful")


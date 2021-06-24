import requests
image_url = "https://cdn.pixabay.com/audio/2020/11/10/audio_547ebbf828.mp3"

r = requests.get(image_url)

filename = "song1"

route = "files/" + "filename" + ".mp3"

with open(route, 'wb') as f:
    f.write(r.content)

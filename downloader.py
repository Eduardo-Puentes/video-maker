import requests
song_url = "https://cdn.pixabay.com/audio/2020/11/10/audio_547ebbf828.mp3"

links = []

for i in range(1):
    links.append(image_url)

for i in range(len(links)):
    r = requests.get(links[i])

    filename = "song" + str(i)

    route = "files/" + filename + ".mp3"

    with open(route, 'wb') as f:
        f.write(r.content)

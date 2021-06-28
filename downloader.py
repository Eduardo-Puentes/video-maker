from selenium import webdriver
from bs4 import BeautifulSoup
from api import API_KEY
import json
import requests


def main():

    # load all the links of the songs
    songs_links = load_songs()
    print("There are " + str(len(songs_links)) + " songs to download")

    # download the songs by his link
    download_songs(songs_links)

    video_links = load_videos()
    print("There are " + str(len(video_links)) + " videos to download")

    download_videos(video_links)


def load_songs():
    go = True
    page = 1
    links = []

    while go:
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")
        driver = webdriver.Chrome(
            executable_path=r'chromedriver_win3\chromedriver.exe', chrome_options=options)
        driver.get(
            'https://pixabay.com/music/search/mood/relaxing/?page=' + str(page))

        html = driver.page_source

        soup = BeautifulSoup(html, "lxml")

        songs = soup.find_all("input", class_="track-source")

        if not songs:
            go = False

        for song in songs:
            links.append(song.get("value"))
            print(song.get("value"))

        page = page + 1

    return links


def download_songs(links):
    for i in range(len(links)):
        r = requests.get(links[i])

        filename = "song" + str(i)

        route = "files/music/" + filename + ".mp3"

        with open(route, 'wb') as f:
            f.write(r.content)

        print("song " + str(i) + " ready!")


def load_videos():
    links = []
    r = requests.get("https://api.pexels.com/videos/search?query=nature&per_page=10", headers={
        'Authorization': API_KEY})

    response = json.loads(r.text)

    for j in response["videos"]:
        found = False
        for k in j["video_files"]:
            if not found and k["quality"] == "hd":
                found = True
                links.append(k["link"])

    return links


def download_videos(links):
    for link in links:
        r = requests.get(link)

        filename = "video" + str(video_count)

        route = "files/video/" + filename + ".mp4"

        with open(route, 'wb') as f:
            f.write(r.content)

        video_count = video_count + 1


if __name__ == "__main__":
    main()

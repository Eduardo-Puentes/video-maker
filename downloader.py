from selenium import webdriver
from bs4 import BeautifulSoup
import requests


def main():

    # load all the links of the songs
    songs_links = load_songs()
    print("There are " + str(len(songs_links)) + " songs to download")

    # download the songs by his link
    download_songs(songs_links)


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

        route = "files/" + filename + ".mp3"

        with open(route, 'wb') as f:
            f.write(r.content)

        print("song " + str(i) + " ready!")


if __name__ == "__main__":
    main()

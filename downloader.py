from selenium import webdriver
from bs4 import BeautifulSoup
import requests

for i in range(2):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    driver = webdriver.Chrome(
        executable_path=r'chromedriver_win3\chromedriver.exe', chrome_options=options)
    driver.get(
        'https://pixabay.com/music/search/mood/relaxing/?page=' + str((i + 1)))

    html = driver.page_source

    soup = BeautifulSoup(html, "lxml")

    songs = soup.find_all("input", class_="track-source")

    links = []

    for song in songs:
        links.append(song.get("value"))

for i in range(len(links)):
    r = requests.get(links[i])

    filename = "song" + str(i)

    route = "files/" + filename + ".mp3"

    with open(route, 'wb') as f:
        f.write(r.content)

    print("song " + str(i) + " ready!")

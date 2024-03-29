from selenium import webdriver
import urllib.request
import json

import requests

PATH = "E:\Polban\Tugas\Semester 2\Proyek\Pertemuan 6\Scrapping 2\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.billboard.com/charts/hot-100/")

from datetime import datetime
x = datetime.now()

billboard = []


for song in driver.find_elements_by_class_name("o-chart-results-list-row"):
    print(song.text)
    for img in song.find_elements_by_class_name("c-lazy-image__img"):


        billboard.append(
            {"current_rank": song.text.split("\n")[0],
            "song_title": song.text.split("\n")[1],
            "singer": song.text.split("\n")[2],
            "last_week_rank": song.text.split("\n")[3],
            "peak_rank": song.text.split("\n")[4],
            "weeks_on_chart": song.text.split("\n")[5],
            "waktu_scraping": x.strftime("%Y-%m-%d pukul %H:%M:%S"),
            "Image": img.get_attribute("src")
            }
            )

scrap = open("scrap.json", "w")
json.dump(billboard, scrap, indent = 6)
scrap.close()
driver.quit()
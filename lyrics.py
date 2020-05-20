import os
import json
import requests
from bs4 import BeautifulSoup


def scrap_song_lyrics(url):
    page = requests.get(url)
    html = BeautifulSoup(page.text, 'html.parser')
    lyrics = html.find('div', class_='lyrics').get_text()

    return lyrics


def request_song_info(song_title, artist_name):
    base_url = 'https://api.genius.com'
    headers = {'Authorization': 'Bearer ' + genius_token}
    search_url = base_url + '/search/'
    data = {'q': song_title + ' ' + artist_name}
    response = requests.get(search_url, data=data, headers=headers)

    return response


def send_thru_script(lyrics):
    lyrics = lyrics.replace("\"", "")
    formatted_content = '"' + \
        lyrics.replace('\n', ' ').replace(" ", ", ") + '"'
    count = len(lyrics.split())
    print("Sending " + str(count) + " texts")
    os.system(f"osascript SendLyrics.scpt {number} {formatted_content} ")


genius_token = '5gCZ4DZEZ-RLoWj3anoMSvXC0ZsR0x99441Gf-LfYh3QH4x4AlvJlw3ygCOuR9Hh'
print("What it doooo\n")
number = input("What is the phone number to send lyrics to? ")
while True:
    stored = input("Do you have the lyrics stored in a file? (y/n) ")
    if stored == "y":
        filename = input("Filename? ")
        with open("songs/" + filename, 'r') as f:
            content = f.read()
        send_thru_script(content)

    if stored == "n":
        song_title = input("What song do you want to send? ")
        artist = input("By which artist? ")
        response = request_song_info(song_title, artist)
        json = response.json()
        info = "qwertyuiopasdfghjkl"
        for hit in json['response']['hits']:
            if artist.lower() in hit['result']['primary_artist']['name'].lower():
                info = hit
                print("Found " + info['result']['title'] +
                      " / " + info['result']['primary_artist']['name'])
                break
        if info != "qwertyuiopasdfghjkl":
            song_url = info['result']['url']
            send_thru_script(scrap_song_lyrics(song_url))
        else:
            repeat = input("Song not found. Send again? (y/n)")
            if repeat == "y":
                continue
            else:
                break

    again = input("Send again (y/n)? ")
    if again == "n":
        break

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

list = []

new_list = []

newest_list = []

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Safari/537.36'}
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/", headers = headers)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all("li", class_="o-chart-results-list__item")
song_names = [song.getText().strip() for song in song_names_spans]

while '' in song_names:
    song_names.remove('')

while '-' in song_names:
    song_names.remove('-')

while 'NEW' in song_names:
    song_names.remove('NEW')

for song in song_names:
    if str(song).isnumeric() == False:
        list.append(song)

for item in list:
    item
    letters = []
    word = ''
    for i in range(len(item)):
        if item[i] != '\t' and item[i] != '\n':
            letters.append(item[i])
    for letter in letters:
        word += letter
    new_list.append(word)

for song in new_list:
    if 'NEW' not in song:
        newest_list.append(song)



base_url = 'https://api.spotify.com/v1'

clientID = 'ca24e70ef438475ab53fc53c5838ff74'
Client_secret = 'b6f11da3989d4cd9919b86e3bd03c3e3'

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/playlist",
        client_id=clientID,
        client_secret=Client_secret,
        show_dialog=True,
        cache_path="token.txt"
    ))
song_list = []
def find_song(query, x):
    results = sp.search(q=query, limit=1)

    try:
        song = results["tracks"]["items"][0]["external_urls"]["spotify"]
        song_list.append(song)
    except:
        pass

x = 0
for song in newest_list:
    x += 1
    find_song(song, x)

playlist_url = f"api.spotify.com/v1/users/{clientID}/playlists"

query = {
    "name": "2022-09-10",
    "public": "false"
}
user_id = sp.current_user()["id"]
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_list)
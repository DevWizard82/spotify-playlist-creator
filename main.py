


import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


#get the top 100 hot songs in the chosen date

date = input("when do you want to travel back to (yyyy-mm-dd): ")


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}", headers=headers)

billboard_webpage = response.text

soup = BeautifulSoup(billboard_webpage, "html.parser")

li_elements = soup.find_all(name="li", class_="o-chart-results-list__item")

songs = []



for li in li_elements:
    song_title = li.find(name="h3", id="title-of-a-story")
    song_artist = li.find(name="span", class_="c-label")
    if song_title and song_artist:
        songs.append(f"{song_title.get_text(strip=True)} - {song_artist.get_text(strip=True)}")



client_id = YOUR_CLIENT_ID
client_secret = YOUR_CLIENT_SECRET


sp_oauth = SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri="https://devwizard82.github.io/response_page/",
    scope="playlist-modify-private",
    show_dialog=True,
    cache_path="token.txt"
)

sp = spotipy.Spotify(auth_manager=sp_oauth)


user_id = sp.current_user()["id"]

song_names = [song.split()[0] for song in songs]


year = date.split("-")[0]

#get the uri links list of the chosen songs

uri_list = []

for song in songs:
    result = sp.search(q=f"track: {song} year: {year}", type="track")

    try:
        uri = result["tracks"]["items"][0]["uri"]
        uri_list.append(uri)

    except IndexError:
        print(f"{song} does not exist in spotify!\n")


#create a playlist

playlist = sp.user_playlist_create(user=user_id, public=False, name=f"{date} Billboard 100")

#add all songs to the playlist

sp.playlist_add_items(playlist_id=playlist["id"], items=uri_list)




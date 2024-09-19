import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

year = int(date.split("-")[0])

URL = "https://www.billboard.com/charts/hot-100/" + date + "/"

response = requests.get(url=URL)

billboard_html = response.text

soup = BeautifulSoup(billboard_html, "html.parser")

titles = soup.select("li ul li h3")

song_titles = [title.getText().strip() for title in titles]

client_id = ""
client_secret = ""

# Define your client ID, client secret, and redirect URI
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri='http://example.com',
    scope="playlist-modify-private"
))

user_id = sp.current_user()["id"]

list_of_available_songs = []

for song in song_titles:
    track = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = track["tracks"]["items"][0]["uri"]
        list_of_available_songs.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist_name = date + " Billboard 100"
playlist_description = 'This playlist was created using Spotipy!'

# Creating the playlist
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False, description=playlist_description)

print(f"Playlist created: {playlist['name']} with ID: {playlist['id']}")

sp.playlist_add_items(playlist_id=playlist["id"], items=list_of_available_songs)

from bs4 import BeautifulSoup
import datetime
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth




sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope='playlist-modify-private',
        cache_path='.cache',
        show_dialog=True
        )
    )









date = input('Year to travel to. YYYY-MM-DD: ')

response = requests.get(f'https://www.billboard.com/charts/hot-100/{date}')
webpage = response.text
soup = BeautifulSoup(webpage, 'lxml')
t = [song.getText().strip() for song in soup.select('li ul li h3')]

year = date.split('-')[0]

song_urls =[]

user_id = sp.current_user()['id']

for song in t:
    song = sp.search(q=f'track:{song}',limit=1, type='track')
    try:
        link = song['tracks']['items'][0]['external_urls']['spotify']
        song_urls.append(link)
    except IndexError:
        print(f'{song} doesnt exist. sorry.')
        

playlist_id = sp.user_playlist_create(user=user_id,name=f'{date} Billboard 100',public=False,description=f'Top 100 songs from {date}. The playlist can only add songs that are on spotify.')['id']


sp.user_playlist_add_tracks(user=user_id,playlist_id=playlist_id,tracks=song_urls)

print('done')

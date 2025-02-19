import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")
SCOPE = "playlist-modify-private playlist-modify-public playlist-read-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE
))

playlist_id = "6XZisdGP9J41IOXeSlayLM"
track_link = "https://open.spotify.com/track/2B4Y9u4ERAFiMo13XPJyGP"
track_id = track_link.split("/")[-1].split("?")[0]
track_uri = f"spotify:track:{track_id}"
def create_playlist(name, description="Новый плейлист", public=False):
    user_id = sp.me()['id']
    playlist = sp.user_playlist_create(user=user_id, name=name, public=public, description=description)
    return playlist['external_urls']['spotify']

def remove_duplicates(playlist_id):
    playlist_id = clean_playlist_id(playlist_id)
    tracks = sp.playlist_items(playlist_id)['items']
    seen = set()
    duplicates = []

    for item in tracks:
        track_id = item['track']['id']
        if track_id in seen:
            duplicates.append(item['track']['uri'])
        else:
            seen.add(track_id)

    if duplicates:
        sp.playlist_remove_all_occurrences_of_items(playlist_id, duplicates)
        return f"{len(duplicates)} дубликатов удалено"
    return "Дубликатов не найдено"

def clean_playlist_id(playlist_id):
    return playlist_id.split("/")[-1].split("?")[0]

def add_to_spotify(playlist_id, track_uris):
    playlist_id = clean_playlist_id(playlist_id)
    sp.playlist_add_items(playlist_id, track_uris)
    return f"{len(track_uris)} треков добавлено"


if __name__ == "__main__":
    print("Создаю новый плейлист...")
    playlist_link = create_playlist("Мой новый плейлист")
    print(f"Ссылка: {playlist_link}")

    test_playlist_id = playlist_link.split("/")[-1]
    print(remove_duplicates(test_playlist_id))

    test_tracks = ['spotify:track:6rqhFgbbKwnb9MLmUQDhG6']
    print(add_to_spotify(test_playlist_id, test_tracks))

    result = add_to_spotify(playlist_id, [track_uri])
    print(result)



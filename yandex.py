from yandex_music import Client
from config import YAN_TOKEN

client = Client(YAN_TOKEN).init()
tracks = {}
for i in client.users_likes_tracks().fetch_tracks():
    if i['type']=='music':
        tracks[i['title']] = i['artists'][0]['name']

        
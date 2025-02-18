from yandex_music import Client
from config import YAN_TOKEN
from rediska import r

client = Client(YAN_TOKEN).init()
tracks = {}
counter = 0
for i in client.users_likes_tracks().fetch_tracks():
    if i['type']=='music':
#        tracks[i['title']] = i['artists'][0]['name']
        
        r.set(f'yandex:{counter}:title',i['title'] )
        r.set(f'yandex:{counter}:artist',i['artists'][0]['name'] )
        counter+=1

        
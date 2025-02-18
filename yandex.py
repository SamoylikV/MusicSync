from yandex_music import Client
from config import YAN_TOKEN
from rediska import r

class Yandex:
    def __init__(self,Token):
        self.token = Token
        self.client = Client(Token).init()
    
    def yan_to_red(self, r):
        
        counter = 0
        for i in self.client.users_likes_tracks().fetch_tracks():
            if i['type']=='music':
        #        tracks[i['title']] = i['artists'][0]['name']
                r.set(f'yandex:{counter}:title',i['title'] )
                r.set(f'yandex:{counter}:artist',i['artists'][0]['name'] )
                counter+=1
        return r.ping()
    
    def likes(self):
        while True:
            counter = 0
            if r.get(f'spotify:{counter}:title') == None:
                break
            title = r.get(f'spotify:{counter}:title')
            artist = r.get(f'spotify:{counter}:artist')
            search_res = self.client.search(f'{artist} {title}')
            if search_res.tracks != None:
                track_id = search_res.tracks['results'][0]['id']
                self.client.users_likes_tracks_add(track_id)
        return r.ping()
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
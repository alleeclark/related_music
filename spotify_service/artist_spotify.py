import requests
import json
from artist import Artist
#curl -X GET "https://api.spotify.com/v1/artists/1RyvyyTE3xzB2ZywiAwp0i"

class Arist_Sportify:
    artist_info = []

    def get_artist_id(self, artist_name):
        artist_name = artist_name[:-1]
        spotify_search_artist = "https://api.spotify.com/v1/search?q=&type=artist"
        isascii = lambda s: len(s) == len(s.encode())
        if isascii(artist_name) == True:
            spotify_search_artist = spotify_search_artist[:36] + artist_name + spotify_search_artist[36:]
            response = requests.get(spotify_search_artist)
            if response.status_code == requests.codes.OK:
                spotify_artist_response = response.json()
                for i in spotify_artist_response['artists']['items']:
                    if artist_name == i['name']:
                        artist_genre = i['genres']
                        artist_name = i['name']
                        self.artist_info = [artist_name,[artist_genre]]
                        return i['id']
            else:
                return False
        else:
            return False

    def get_related_artist(self, artist_name):
        artist_id = self.get_artist_id(artist_name)
        list_of_related = []
        spotify_related_url = "https://api.spotify.com/v1/artists//related-artists"
        if artist_id != None:
            spotify_related_url = spotify_related_url[:35] + artist_id + spotify_related_url[35:]
            print(spotify_related_url)
        else:
            return False
        response = requests.get(spotify_related_url)
        if response.status_code == requests.codes.OK:
            spotify_related_response = response.json()
            for i in spotify_related_response['artists']:
                # maybe get ids too
                related_artist_name = i['name']
                list_of_related = [related_artist_name]
                self.artist_info = self.artist_info + list_of_related
        else:
            return False
        return self.artist_info
                


future = "Future"
something = Artist()
testing = Arist_Sportify()
what = something.get_list_of_names()
for i in what:
    print(testing.get_related_artist(i))
wow = testing.get_related_artist(future)
j = json.dumps(wow)
#print(j)
import requests
import json
import string
from artist import Artist

class lastfm_rest_service:

    def get_lastfm_url(self, artist_name):
        lastfm_url ='http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist=&api_key=bae243fa08eccb50f4884d67fdc54b20&format=json'
        isascii = lambda s: len(s) == len(s.encode())
        if isascii(artist_name) == True:
            return lastfm_url[:63] + artist_name + lastfm_url[63:]
        else:
            return False
    
    def get_artist_info(self, artist_name):
        url = self.get_lastfm_url(artist_name)
        response = requests.get(url)
        if response.status_code == requests.codes.OK:
            artist_response = response.json()
            lastfm_artist_name = artist_response['artist']['name']
            playcount = artist_response['artist']['stats']['playcount']
            listeners_count = artist_response['artist']['stats']['listeners']
            # continue to add whatever attributes you want
            # add them to some kind of key vlaue pair 
            # return that dictionary
        else:
            return False

brick = lastfm_rest_service()
print(brick.get_lastfm_url(name))

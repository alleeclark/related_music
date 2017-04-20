import requests
import json
import string
from artist import Artist

class lastfm_rest_service:

    def get_info(self, artist_name):
        lastfm_url ='http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist=&api_key=bae243fa08eccb50f4884d67fdc54b20&format=json'
        isascii = lambda s: len(s) == len(s.encode())
        if isascii(artist_name) == True:
            return lastfm_url[:63] + artist_name + lastfm_url[63:]
        else:
            return False

    #similar function as above but with different url 
    def get_top_tags(self, artist_name):
        lastfm_url ='http://ws.audioscrobbler.com/2.0/?method=artist.getTopTags&artist=&api_key=bae243fa08eccb50f4884d67fdc54b20&format=json'
        isascii = lambda s: len(s) == len(s.encode())
        if isascii(artist_name) == True:
            return lastfm_url[:66] + artist_name + lastfm_url[66:]
        else:
            return False
    
    def get_artist_info(self, artist_name):
        url_get_info = self.get_info(artist_name)
        response_get_info = requests.get(url_get_info)

        url_top_tags = self.get_top_tags(artist_name)
        response_top_tags = requests.get(url_top_tags)

        if response_get_info.status_code == requests.codes.OK:
            artist_response = response_get_info.json()
            lastfm_artist_name = artist_response['artist']['name']
            playcount = artist_response['artist']['stats']['playcount']
            listeners_count = artist_response['artist']['stats']['listeners']
            similiar_1 = artist_response['artist']['similar']['artist'][0]['name']
            similiar_2 = artist_response['artist']['similar']['artist'][1]['name']
            similiar_3 = artist_response['artist']['similar']['artist'][2]['name']
            #artist dictionary
            artist_dic = {}
            artist_dic[artist_name] = {}
            artist_dic[artist_name] = [playcount, listeners_count]
            artist_dic[artist_name].append({'Similar':[similiar_1, similiar_2, similiar_3]})
            #tag dictionary subset of artist dictionary
            if response_top_tags.status_code == requests.codes.OK:
                top_tags = response_top_tags.json()
                tag_length = len(top_tags['toptags']['tag'])
                tag_1 = top_tags['toptags']['tag'][0]['name']
                tag_2 = top_tags['toptags']['tag'][1]['name']
                tag_3 = top_tags['toptags']['tag'][2]['name']
                artist_dic[artist_name].append({'Tags':[tag_1, tag_2, tag_3]})
            else:
                return False
            
            return artist_dic
        else:
            return False

    #convert to json
    def final_artist_dic(self, artist_name):
        artist_dic = self.get_artist_info(artist_name)
        final_artist_dic = json.dumps(artist_dic)
        return final_artist_dic

# brick = lastfm_rest_service()
# print(brick.final_artist_dic('Snoop Dogg'))



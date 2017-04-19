import requests
import json
import string
from artist import Artist


class lastfm_rest_service:
    artist_dictionary = {}

    def get_lastfm_url(artist_name):
        #url = 'http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist=Rick Ross&api_key=bae243fa08eccb50f4884d67fdc54b20&format=json'
        lastfm_url ='http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist=&api_key=bae243fa08eccb50f4884d67fdc54b20&format=json'
        for letter in artist_name:
            if letter not in string.ascii_letters:
                return lastfm_url[:63] + artist_name + lastfm_url[63:]
            else:
                return False
    
    def get_artist_info(self, artist_name):
        response = requests.get(self.get_lastfm_url())
        if response.status_code == requests.codes.OK:
            # not parsing right 
            artist_dic = response.json()['artist']
            playcount = artist_dic['stats']['playcount']
            listeners_count = artist_dic['stats']['listeners']
            self.artist_dictionary[]
            return self.artist_dictionary[artist_dic] =       
            


    
                
brick = lastfm_rest_service()
brick.get_lastfm_url()            

#artist_list = ['100 Kila','100s','12 Gauge','2 Chainz']
# def artist_data(artist_list):
#     artist_dic_final = {}
#     file = 'http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist=100 Kila&api_key=bae243fa08eccb50f4884d67fdc54b20&format=json'
#     for i in range(len(artist_list)):
#         #file text manipulation
#         file_str = file.split('&')
#         file_str[1] = 'artist=' + artist_list[i]
#         file_str = '&'.join(file_str)
        
#         #last fm dictionary/data pull
#         response = requests.get(file_str)
#         artist_dic = response.json()['artist']
#         play_count = artist_dic['stats']['playcount']
#         listeners_count = artist_dic['stats']['listeners']
        
#         if not artist_list[i]  in artist_dic_final:
#             artist_dic_final[artist_list[i]] = {}
        
#         artist_dic_final[artist_list[i]]['play_count'] = play_count
#         artist_dic_final[artist_list[i]]['listeners_count'] = listeners_count
        
#     return artist_dic_final
# print(artist_data(artist_list))
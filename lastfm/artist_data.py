import requests
import json

artist_list = ['100 Kila','100s','12 Gauge','2 Chainz']
def artist_data(artist_list):
    artist_dic_final = {}
    file = 'http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist=100 Kila&api_key=bae243fa08eccb50f4884d67fdc54b20&format=json'
    for i in range(len(artist_list)):
        #file text manipulation
        file_str = file.split('&')
        file_str[1] = 'artist=' + artist_list[i]
        file_str = '&'.join(file_str)
        
        #last fm dictionary/data pull
        response = requests.get(file_str)
        artist_dic = response.json()['artist']
        play_count = artist_dic['stats']['playcount']
        listeners_count = artist_dic['stats']['listeners']
        
        if not artist_list[i]  in artist_dic_final:
            artist_dic_final[artist_list[i]] = {}
        
        artist_dic_final[artist_list[i]]['play_count'] = play_count
        artist_dic_final[artist_list[i]]['listeners_count'] = listeners_count
        
    return artist_dic_final
print(artist_data(artist_list))
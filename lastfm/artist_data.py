import requests
import json
import artist

artist_list = artist.Artist().get_list_of_names()
# print(artist_list)
# artist_list = ['Frank Ocean']

def artist_data(artist_list):
    artist_dic_final = {}
    file1 = 'http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist=100 Kila&api_key=bae243fa08eccb50f4884d67fdc54b20&format=json'
    for i in range(len(artist_list)):
        #file text manipulation
        file_str = file1.split('&')
        file_str[1] = 'artist=' + artist_list[i]
        file_str = '&'.join(file_str).encode('utf-8')
        #last fm dictionary/data pull
        response = requests.get(file_str)
        # artist_dic = response.json()
        artist_dic = response.json()['artist']
        play_count = artist_dic['stats']['playcount']
        listeners_count = artist_dic['stats']['listeners']
        
        if not artist_list[i]  in artist_dic_final:
            artist_dic_final[artist_list[i]] = {}
        artist_dic_final[artist_list[i]] = artist_dic
        
        artist_dic_final[artist_list[i]]['play_count'] = play_count
        artist_dic_final[artist_list[i]]['listeners_count'] = listeners_count
        
    return artist_dic_final
    # return file_str
print(artist_data(artist_list))
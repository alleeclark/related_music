import artist_data
import artist

# test = artist.Artist()
# test_artists = test.get_list_of_names()
f = open('C:/Users/danil/Documents/GitHub/related_music/lastfm/artistlist.txt', encoding = 'UTF-8')
f_list = f.read().splitlines()
artist_data1 = artist_data.lastfm_rest_service()
# print(f_list)
for i in range(len(f_list)):
    try:
        print (artist_data1.final_artist_dic(f_list[i]))
    except:
        print('Not found')
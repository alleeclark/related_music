import bisect

class Artist(object):
    f = open('/home/allee/Projects/mlmusic/music_services/lastfm/artistlist.txt', 'r')
    names = []

    def __init__(self):
        f = open('/home/allee/Projects/mlmusic/music_services/lastfm/artistlist.txt', 'r')
        names = []
      
    def print_list_of_names(self):
        for name in self.f:
            print(name, end='')

    def get_list_of_names(self):
        for name in self.f:
            self.names.append(name)
        return self.names

    def search_names(self, artist_name):
        listed = self.get_list_of_names()
        lower_bound = 0 
        upper_bound = len(listed)
        while True:
            if lower_bound == upper_bound:
                return -1
            mid_index = (lower_bound+upper_bound) //2
            item_at_mid = listed[mid_index]
            if item_at_mid == artist_name:
                return mid_index
            if item_at_mid < artist_name:
                lower_bound = mid_index + 1
            else:
                upper_bound = mid_index
                
#this still needs some work
    def add_to_list_of_names(self, artist_name):
        if self.search_names(artist_name) == -1:
            #new_list = bisect.insort(self.get_list_of_names(), artist_name)
            old_list =self.get_list_of_names()
            inserted_list = [artist_name]
            new_list = self.mergelist(inserted_list)
            print(new_list)
            self.f = open('/home/allee/Projects/mlmusic/music_services/lastfm/artistlisttest.txt', 'w')
            for i in new_list:
                self.f.write(i)
            print("added")
            self.f = close()
        else:
            print("artist already in the list")
#need some work
    def mergelist(self, new_artist):
        old = self.get_list_of_names()
        result = []
        xi = 0
        yi = 0

        while True:
            if xi > len(old):
                result.extend(new_artist[yi:])
                return result
            
            if yi >= len(new_artist):
                result.extend(old[xi:])
                return result
            
            if old[xi:] <= new_artist[yi]:
                result.append(new_artist[xi])
                xi += 1
            else:
                result.append(new_artist[yi])
                yi += 1

    def test_script(this_object):
        this_object.list_of_names()

testscript = Artist()
artz = "Asaad"
print(testscript.add_to_list_of_names(artz))
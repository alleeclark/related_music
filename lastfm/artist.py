class Artist(object):
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

    def test_script(this_object):
        this_object.list_of_names()
    
testscript = Artist()
artistz = "Future"
testscript.print_list_of_names()
import redis
import artist_data

brick = artist_data.lastfm_rest_service()
output = brick.final_artist_dic('Snoop Dogg')

r = redis.StrictRedis.from_url('redis://user:pass@hostid/0')
result = r.set('Snoop Dogg',output)
# print(r.get('foo1'))
print(r.get('Snoop Dogg'))
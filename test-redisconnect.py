import redis
r = redis.StrictRedis.from_url('redis://user:passwoard@connection/0')
result = r.get('foo')
print(result)
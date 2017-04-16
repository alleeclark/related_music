import redis
r = redis.StrictRedis.from_url('redis://user:passwoard@connection/0')
r.flushdb()
result = r.get('foo')
print(result)
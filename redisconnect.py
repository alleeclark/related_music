import redis
r = redis.StrictRedis.from_url('redis://user:XcDu53Ss@104.198.232.121:6379/0')
r.flushdb()
result = r.get('foo')
print(result)
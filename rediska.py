import redis

r = redis.Redis(
    host='127.0.0.1',
    port=6379,
    db=0, # 0-15
    decode_responses=True,
    password='mypassword'
)
print(r.ping())
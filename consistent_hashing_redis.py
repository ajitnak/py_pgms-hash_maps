import redis
cr = = ConsistentHashRing(100)

cr["node1"] = redis.StrictRedis(host="host1")
cr["node2"] = redis.StrictRedis(host="host2")

client = cr["some key"]
data = client.get("some key")

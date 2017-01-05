import redis
# create a connection to the localhost Redis server instance, by
# default it runs on port 6379
redis_db = redis.StrictRedis(host="localhost", port=6379, db=0)
# see what keys are in Redis
print "keys", redis_db.keys()
# output for keys() should be an empty list "[]"
print redis_db.set('full stack', 'python')
# output should be "True"
print redis_db.keys()
# now we have one key so the output will be "[b'full stack']"
print redis_db.get('full stack')
# output is "b'python'", the key and value still exist in Redis
print redis_db.incr('twilio')
# output is "1", we just incremented even though the key did not
# previously exist
print redis_db.get('twilio')
# output is "b'1'" again, since we just obtained the value from
# the existing key
print redis_db.delete('twilio')
# output is "1" because the command was successful
print redis_db.get('twilio')
# nothing is returned because the key and value no longer exist

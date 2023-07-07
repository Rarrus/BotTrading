import redis

redis_host = "database-1.cjoanwq1hzdw.eu-west-2.rds.amazonaws.com"
redis_port = 3306

redis_client = redis.Redis(host=redis_host, port=redis_port)

# Set a value
redis_client.set('key', 'value')

# Get a value
value = redis_client.get('key')
print(value)


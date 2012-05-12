import os
import urlparse

import redis

url = urlparse.urlparse(os.environ.get('REDISTOGO_URL', 'redis://localhost'))

redis = redis.Redis(host=url.hostname, port=url.port, db=0, password=url.password)
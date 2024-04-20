from flask import Flask 
from redis import Redis as redisClient

r = redisClient(host='localhost',port='6379')
app = Flask(__name__)


@app.route('/')
def initial():
    visits = redisClient.get('visits')
    redisClient.set('visits', int(++visits))
    return f''' 
    here is the time this site was visited {visits}
    '''

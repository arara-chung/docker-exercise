from flask import Flask, render_template, request
import redis

app = Flask(__name__)
default = '1'
cache = redis.StrictRedis(host='redis', port=6379, db=0)
cache.set(default, 'one-one-one')

@app.route('/', methods=['GET', 'POST']) 
def hello():
    
    key = default
    if 'key' in request.form:
        key = request.form['key']

    if request.method == 'POST' and request.form['submit'] == 'save':
        cache.set(key, request.form['cache_value'])

    cache_value = None
    if cache.get(key):
        cache_value = cache.get(key).decode('utf-8')

    return render_template('index.html', key=key, cache_value=cache_value)

if __name__ == '__main__':
    app.run(host='0.0.0.0')



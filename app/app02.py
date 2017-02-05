from flask import Flask, render_template, request

app = Flask(__name__)
default = '1'
cache = {default: 'one-one-one'}

@app.route('/', methods=['GET', 'POST']) 
def hello():
    
    key = default
    if 'key' in request.form:
        key = request.form['key']

    if request.method == 'POST' and request.form['submit'] == 'save':
        cache[key] = request.form['cache_value']

    cache_value = None
    if key in cache:
        cache_value = cache[key]

    return render_template('index.html', key=key, cache_value=cache_value)

if __name__ == '__main__':
    app.run(host='0.0.0.0')



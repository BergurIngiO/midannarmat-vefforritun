from bottle import run, route, template, static_file, error
import requests
import os

response = requests.get('http://apis.is/petrol')
data = response.json()

@route('/')
def index():
    return template('index', data=data)

@route('/company/<{{c}}>')
def companie(c):
    return template('companie', c=c, data=data)

@route('/static/<filename>')
def static_server(filename):
    return static_file(filename, root='./static_files')

@error(404)
def error404(error):
    return '<h1> Sidan er ekki til</h1>'

@error(500)
def error500(error):
    return '<h1> Villa a midlara </h1>'

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
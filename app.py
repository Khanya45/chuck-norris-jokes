from flask import Flask
import requests


app = Flask(__name__)


@app.route('/', methods=['GET'])
def projects_page():
    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url).json()
    return \
        f'<img src="{response["icon_url"]}">' \
        f'<h2>ID: {response["id"]}</h2>' \
        f' <h3>Date: {response["created_at"]}</h3>' \
        f'<h2>Random jokes</h2>' \
        f' <p>{response["value"]}</p>'


@app.route('/category', methods=['GET'])
def category():
    html = ""
    api_url = "https://api.chucknorris.io/jokes/categories"
    response = requests.get(api_url).json()
    for i in response:
        html += f'<h2>{i}<h2>\n'
    return html



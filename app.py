from flask import Flask
from flask import request


app = Flask(__name__)


@app.route('/', methods=["GET"])
def projects_page():
    api_url = "https://api.chucknorris.io/jokes/random"
    response = request.get(api_url).json()
    return \
        f'<img src="{response["icon_url"]}">' \
        f'<h3>ID: {response["id"]}' \
        f'<h3> Date it was created: {response["created_at"]}</h3>' \
        f'<strong> Random joke:</strong>{response["value"]}'


if __name__ == '__main__':
    app.debug = True
    app.run()

from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    # Make a GET request to a sample API
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        title = data.get('title', 'Title not found')
    else:
        title = 'Unable to fetch title'

    return f"Hello, {title}!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
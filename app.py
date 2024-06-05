from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    name = os.getenv("NAME", "World")
    return f'Hello, {name} you are amazing!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
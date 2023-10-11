from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!if I fully understand this you are finished'

if __name__ == '__main__':
    app.run(debug = True)
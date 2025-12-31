from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World! This is my Flask app running on EC2.'

if __name__ == '__main__':
    # We set host to 0.0.0.0 so it's accessible outside the container
    app.run(host='0.0.0.0', port=5000)

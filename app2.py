from flask import Flask, request, json
app = Flask(__name__)


@app.route('/', methods = ['GET'])
def root():
    return "hello world_2"

if __name__== "__main__":
    host='127.0.0.1'
    port=4901
    app.run(host=host, port=port)

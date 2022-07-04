from flask import Flask

PORT = "1128"
HOST = "127.0.0.1"

app = Flask(__name__)

@app.route('/')
def helloFlask():
    return '플라스크 지금부터 시작!'

if __name__ == '__main__':
    app.run(host = HOST, port = PORT, debug=True)
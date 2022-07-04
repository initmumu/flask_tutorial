from flask import Flask
from flask import Blueprint


PORT = "1128"
HOST = "127.0.0.1"


app = Flask(__name__)
from ROUTE import home

app.register_blueprint(home.bp)



if __name__ == '__main__':
    app.run()
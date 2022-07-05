from flask import Flask, render_template

PORT = "1128"
HOST = "127.0.0.1"

app = Flask(__name__)
@app.route('/')
def helloFlask():
    return render_template('main.html')

@app.route('/login')
def loginPage():
    return render_template('login.html')

if __name__ == '__main__':
    app.run()
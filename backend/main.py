from flask import Flask, request

app = Flask(__name__)

@app.route('/sigin', methods=['POST'])
def sigin():
    user_mail = request.headers.get('email')
    print(data)
    return 'ok'
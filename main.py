from flask import Flask, send_file, jsonify

app = Flask(__name__)

@app.route('/form', methods=['GET'])
def form():
    with open('./form.html', 'r', encoding='utf-8') as f:
        text = f.read()
    return text

@app.route('/Omnie', methods=['GET'])
def Omnie():
    with open('./Omnie.html', 'r', encoding='utf-8') as f:
        text = f.read()

    return text

@app.route('/style', methods=['GET'])
def style():
    with open('./style.css', 'r') as f:
        text = f.read()

    return app.send_static_file ('text')

@app.route('/profilowe.jpg', methods=['GET'])
def f():
    return send_file('./profilowe.jpg', mimetype='image/jpeg')

@app.route('/Omnie', methods=['POST'])
def post_message():
    return "OK"


app.run(port=3000, host="0.0.0.0")

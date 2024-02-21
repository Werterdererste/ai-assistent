import flask
from flask import Flask, render_template, request


app = Flask(__name__)
massages = list(())


class WebInterface:

    def __init__(self, port: int):
        self.port = port

    def start(self):
        app.run(host='127.0.0.1', port=self.port)


@app.route('/')
def index():
    return flask.redirect('/chat')


@app.route('/chat', methods=['POST', 'GET'])
def chat_post():
    if request.method == 'POST':
        prompt = request.form['prompt']
        massages.append((prompt, "antwort"))

        ausgabe = ""
        for massage in massages:
            ausgabe += "Frage: " + massage[0] + "\n Antwort: " + massage[1]
        return render_template('chat.html', response=ausgabe)

    else:
        return render_template('chat.html')


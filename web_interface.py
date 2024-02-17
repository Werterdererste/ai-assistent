from flask import Flask, render_template, request
app = Flask(__name__)

class WebInterface:

    def __init__(self, port: int):
        self.port = port

    def start(self):
        app.run(host='127.0.0.1', port=self.port)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['GET'])
def chat_prompt():
    if request.form['prompt'] is not None:
        return "true"
    else:
        return render_template("chat.html")

from models import IModels

from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)


class WebInterface:

    def __init__(self, port: int, model: IModels):
        self.port = port
        self.model = model
        self.setup_routes()

    def start(self):
        app.run(host='127.0.0.1', port=self.port)

    def setup_routes(self):
        @app.route('/')
        def index():
            return redirect('/chat')

        @app.route('/chat')
        def chat_post():
            return render_template('chat.html')

        @app.route('/api/model', methods=['POST', 'GET'])
        def api_model():
            if request.method == 'POST':
                prompt = request.form['prompt']

                answer = self.model.send(prompt)
                print(answer)
                data = {
                    "prompt": prompt,
                    "answer": answer
                }

                return json.dumps(data)
            else:
                return "Error"

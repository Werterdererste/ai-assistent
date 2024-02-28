from models import IModels

from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)


class WebInterface:
    """
    web Interfache
    """
    def __init__(self, port: int, model: IModels):
        self.port = port
        self.model = model
        self.setup_routes()

    def start(self):
        """
        startet den web assistenten
        localhost und out
        :return:
        """

        app.run(host='127.0.0.1', port=self.port)
        app.run(host='0.0.0.0', port=self.port)

    def setup_routes(self):
        """
        web app
        :return:
        """
        @app.route('/')
        def index():
            """
            index umleitung
            :return:
            """
            return redirect('/chat')

        @app.route('/chat')
        def chat_post():
            """
            zeigt chat an
            :return:
            """
            return render_template('chat.html')

        @app.route('/api/model', methods=['POST', 'GET'])
        def api_model():
            """
            api schnittstelle für js
            :return:
            """
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
                data = {
                    "prompt": "?",
                    "answer": "there was an error"
                }
                return json.dumps(data)

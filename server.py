from flask import Flask, request, jsonify, send_from_directory
from langchain_community.llms import Ollama
import os

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/invoke', methods=['POST'])
def invoke():
    data = request.json
    model_name = data.get('model')
    user_input = data.get('input')

    try:
        llm = Ollama(model=model_name)
        result = llm.invoke(user_input)
        return jsonify({'result': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

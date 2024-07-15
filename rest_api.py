from flask import Flask, Response
import json
import os

app = Flask(__name__)

# JSON dosyasından veriyi okuma
def read_data():
    file_path = os.path.join(os.path.dirname(__file__), 'kafka_data.json')
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

@app.route('/data', methods=['GET'])
def get_data():
    data = read_data()
    response = Response(
        json.dumps(data, ensure_ascii=False),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == "__main__":
    app.run(debug=True, port=8080)

from flask import Flask, render_template, request, jsonify

APP_PORT = 5100

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    resp = jsonify(health="healthy")
    resp.status_code = 200
    return resp

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

print("🚀 Starting Application at the Port", APP_PORT)
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=APP_PORT)

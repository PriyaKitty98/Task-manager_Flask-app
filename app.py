from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Task Manager API Running 🚀"

@app.route('/health')
def health():
    return jsonify({"status": "OK"})

if __name__ == '__main__':
    app.run(debug=True)

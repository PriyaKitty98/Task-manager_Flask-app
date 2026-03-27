from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Final Rebase Version"

@app.route('/health')
def health():
    return jsonify({"status": "OK"})

if __name__ == '__main__':
    app.run(debug=True)

tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    task = {"id": len(tasks)+1, "name": "Sample Task"}
    tasks.append(task)
    return jsonify(task)

@app.route('/login')
def login():
    return "Login API Coming Soon"
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/control', methods=['POST'])
def control_robot():
    data = request.json
    command = data.get('command')
    print(f"Received command: {command}")
    return jsonify({"status": "success", "command": command})

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify

app = Flask(_name_)

# Variabel global untuk menyimpan suhu
current_temperature = None

@app.route('/temperature', methods=['POST'])
def receive_temperature():
    global current_temperature
    data = request.get_json()
    if 'temperature' in data:
        current_temperature = data['temperature']
        print(f"Received temperature: {current_temperature} °C")
        return jsonify({'message': 'Temperature received'}), 200
    else:
        return jsonify({'message': 'No temperature in data'}), 400

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000, debug=True)

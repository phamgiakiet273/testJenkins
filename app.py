from flask import Flask, jsonify, request

app = Flask(__name__)

# Route to get the current version
@app.route('/get_version', methods=['GET'])
def get_version():
    return jsonify({"version": "1.0.0"}), 200

# Route to check if a number is prime
@app.route('/check_prime', methods=['GET'])
def check_prime():
    number = request.args.get('number', type=int)
    if number is None:
        return jsonify({"error": "Number is required"}), 400

    if number < 2:
        return jsonify({"number": number, "is_prime": False}), 200

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return jsonify({"number": number, "is_prime": False}), 200

    return jsonify({"number": number, "is_prime": True}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

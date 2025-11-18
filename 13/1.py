import json

from flask import Flask, Response, jsonify

app = Flask(__name__)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 2) + 1):
        if num % i == 0:
            return False
    return True

@app.route('/prime_number/<number>')
def prime_number(number):
    try:
        num = int(number)
    except ValueError:
        return jsonify({"message": "Invalid number"}), 400
    prime = is_prime(num)
    response = {
        "Number": num,
        "isPrime": prime
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=False, use_reloader=True, host='127.0.0.1', port=5000)

from flask import Flask, jsonify, request
from werkzeug.exceptions import BadRequest

app = Flask(__name__)


@app.route('/sort', methods=['POST'])
def sort_list():
    status = 400

    try:
        req_numbers = request.get_json()
    except BadRequest:
        return "Only JSON requests are allowed with this format= [1,2,3,4,5]", status

    if not req_numbers:
        response = 'Error: Request is empty'
    else:
        status = 200
        response = sorted(req_numbers)

    return jsonify(response), status


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/data')
def data():
    return jsonify({'name': 'john', 'age': 30})


if __name__ == '__main__':
    app.run(debug=True)

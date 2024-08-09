from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('form.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return f'Thank You, {name}!'


if __name__ == '__main__':
    app.run(debug=True)

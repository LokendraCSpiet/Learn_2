from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    # return "Welcome to the Home Page!"
    return render_template('home.html')


@app.route('/about')
def about():
    # return "Welcome to the About Page!"
    return render_template('about.html')


@app.route('/contact')
def contact():
    # return "Welcome to the Contact Page!"
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)

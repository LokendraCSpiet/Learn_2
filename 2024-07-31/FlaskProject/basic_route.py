from flask import Flask

# App Creation File
app = Flask(__name__)


# routes File
@app.route('/')
def home():
    return "Welcome to the Home Page!"


# run file
if __name__ == '__main__':
    app.run(debug=True)

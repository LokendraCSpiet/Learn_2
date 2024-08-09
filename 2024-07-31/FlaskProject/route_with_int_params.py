from flask import Flask

app = Flask(__name__)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post ID: {post_id}'


if __name__ == '__main__':
    app.run(debug=True)
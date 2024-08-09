from flask import Flask, render_template

app = Flask(__name__)


@app.route('/items')
def items():
    item_list = ['Apple', 'Orange', 'Banana', 'Grapes']
    return render_template('item.html', items=item_list)


# run file
if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# sample data
items = [
    {"id": 1, "first_name": "Emp 1", "last_name": "lname 1", 'address': 'add 1'},
    {"id": 2, "first_name": "Emp 2", "last_name": "lname 1", 'address': 'add 2'},
    {"id": 3, "first_name": "Emp 3", "last_name": "lname 1", 'address': 'add 3'},
]


# Route to get all item
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)


# Route to get a single item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({'messages': 'Item not found'}), 404
    return jsonify(item)


# Route to create a new item
@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or 'first_name' not in request.json:
        abort(400)
    item = {
        'id': items[-1]['id'] + 1,
        'first_name': request.json['first_name'],
        'last_name': request.json['last_name'],
        'address': request.json['address']
    }
    items.append(item)
    return jsonify(item), 201  # Removed the trailing comma


@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({'message': 'Item not found'}), 404
    if not request.json:
        abort(400)
    if 'first_name' in request.json and type(request.json['first_name']) != str:
        abort(400)
    if 'last_name' in request.json and type(request.json['last_name']) != str:
        abort(400)
    if 'address' in request.json and type(request.json['address']) != str:
        abort(400)
    item['first_name'] = request.json.get('first_name', item['first_name'])
    item['last_name'] = request.json.get('last_name', item['last_name'])
    item['address'] = request.json.get('address', item['address'])
    return jsonify(item)


@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True)

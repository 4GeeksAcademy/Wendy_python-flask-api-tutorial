from flask import Flask, jsonify, request

app = Flask(__name__)
todos=[ { "label": "My first task", "done": False } ]




@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)



@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    print("This is the position to delete:", position)
    return jsonify(todos)


@app.route('/todos/<int:position>', methods=['PUT'])
def update_new_todo(position):
    request_body = request.json
    todos[position]=request_body
    return jsonify(todos)
    







# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3200, debug=True)
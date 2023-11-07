from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

@app.route('/hello', methods=['GET'])
def hello_get():
    """
    This endpoint returns a greeting message.
    ---
    parameters:
      - name: fname
        in: query
        type: string
        required: false
        default: Default
      - name: lname
        in: query
        type: string
        required: false
        default: User
    responses:
      200:
        description: A greeting message
    """
    firstname = request.args.get('fname', 'Default')
    lastname = request.args.get('lname', 'User')
    return f'Hello {firstname} {lastname}!'

if __name__ == '__main__':
    app.run(debug=True)
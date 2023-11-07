from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/greeting', methods=['GET'])
def hello_get():
    name = request.args.get('name', 'Default User')
    return jsonify({'message': f'Hello {name}!'})

if __name__ == '__main__':
    app.run(debug=True)
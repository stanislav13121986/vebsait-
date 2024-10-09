from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('reg.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    car_model = data.get('car_model')
    return jsonify({'message': 'Регистрация на тест-драйв успешна!', 'name': name, 'car_model': car_model})

if __name__ == '__main__':
    app.run(debug=True)
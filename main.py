from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/conversor')
def conversor():
    return render_template('conversor.html')

@app.route('/api', methods=['GET'])
def api():
    # Example API endpoint that returns a JSON response
    data = request.get_json()
    valor_desejado = data.get('valor_desejado', 0)
    return jsonify({"value": 100})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
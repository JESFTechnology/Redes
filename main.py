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

@app.route('/api', methods=['POST'])
def api():
    # Example API endpoint that returns a JSON response
    data : dict = request.get_json()
    valor_a_converter = data.get('value', 0)
    tipo_a_converter = data.get('type', 0)

    resultado_dos_conversores = {
        "bin": 0,
        "dec": 0,
        "hex": 0,
        "error":False
    }

    from tools.conversor import Hex, Bin, Dec

    match tipo_a_converter:
        case "bin":
            bin_conversor = Bin(valor_a_converter)
            resultado_dos_conversores["error"], resultado_dos_conversores["dec"] = bin_conversor.to_dec()
            resultado_dos_conversores["bin"] = valor_a_converter
            resultado_dos_conversores["error"], resultado_dos_conversores["hex"] = bin_conversor.to_hex()

        case "dec":
            # Converter de decimal para binário
            dec_conversor = Dec(int(valor_a_converter))
            resultado_dos_conversores["dec"] = valor_a_converter
            resultado_dos_conversores["error"], resultado_dos_conversores["bin"] = dec_conversor.to_bin()
            resultado_dos_conversores["error"], resultado_dos_conversores["hex"] = dec_conversor.to_hex()
            
        case "hex":
            # Converter de hexadecimal para decimal
            hex_conversor = Hex(valor_a_converter)
            resultado_dos_conversores["error"], resultado_dos_conversores["dec"] = hex_conversor.to_dec()
            resultado_dos_conversores["error"], resultado_dos_conversores["bin"] = hex_conversor.to_bin()
            resultado_dos_conversores["hex"] = valor_a_converter

    return jsonify(resultado_dos_conversores)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
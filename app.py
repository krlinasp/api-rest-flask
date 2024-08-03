from flask import Flask, jsonify, request
import math

app = Flask(__name__)

def volumen_esfera(radio):
    volumen = (4/3) * math.pi*radio**3
    return volumen

def volumen_cilindro(radio, altura):
    volumen = math.pi*radio**2*altura
    return volumen
    
@app.route('/convert', methods = ['POST'])
def convert_radio():
    data = request.get_json()
    input_radio=data.get('radio')
    input_altura = data.get('altura')
    
    if data['altura'] == 0:
        result = volumen_esfera(input_radio)
    if data['altura'] > 0:
        result = volumen_cilindro(input_radio, input_altura)
             
    return jsonify({"El volumen es": result})

if __name__ == '__main__':
    app.run(debug=False)
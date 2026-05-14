from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from analysis import analyze_stock

# Path synchronized with your "Frontend" folder name
app = Flask(__name__, 
            template_folder='../Frontend', 
            static_folder='../Frontend', 
            static_url_path='')

CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    ticker = data.get('stock')
    
    if not ticker:
        return jsonify({"error": "No ticker provided"}), 400
        
    result, error = analyze_stock(ticker)
    
    if error:
        return jsonify({"error": error}), 400
        
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
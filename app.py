from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Fungsi untuk menghitung rekomendasi gizi
def calculate_nutrition(data):
    # Simulasi perhitungan gizi
    recommended = {
        "calories": 2000,
        "protein": 50,
        "carbs": 300,
        "fat": 70
    }
    return recommended

@app.route('/')
def home():
    # Render halaman HTML test.html
    return render_template('test.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    # Ambil data dari frontend
    input_data = request.json
    if not input_data:
        return jsonify({"error": "No input data provided"}), 400
    
    # Hitung rekomendasi gizi
    recommendations = calculate_nutrition(input_data)
    return jsonify(recommendations)

@app.route('/')
def home():
    return render_template('test.html')  # Halaman utama

@app.route('/article')
def article():
    return render_template('article.html')  # Halaman artikel

@app.route('/contact')
def contact():
    return render_template('contact.html')  # Halaman kontak

if __name__ == '__main__':
    app.run(debug=True)

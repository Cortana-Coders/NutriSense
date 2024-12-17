from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Halaman utama

@app.route('/kalkulator_gizi')
def kalkulator_gizi():
    return render_template('kalkulator_gizi.html')  # Halaman artikel

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/404_page')
def error_page():
    return render_template('404_page.html')

@app.route('/privacy_police')
def privacy_police():
    return render_template('privacy_police.html')



if __name__ == '__main__':
    app.run(debug=True)

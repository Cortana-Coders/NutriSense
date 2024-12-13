from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Model untuk item
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

@app.route('/')
def index():
    items = Item.query.all()  # Ambil semua data
    return render_template('index.html', items=items)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/calculator')
def calculator():
    return render_template('calculator.html')

@app.route('/articles')
def articles():
    return render_template('articles.html')

@app.route('/add', methods=['POST'])
def add():
    name = request.form.get('name')
    new_item = Item(name=name)
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for('index'))  # Redirect ke homepage setelah menambah item

if __name__ == '__main__':
    db.create_all()  # Membuat tabel jika belum ada
    app.run(debug=True)

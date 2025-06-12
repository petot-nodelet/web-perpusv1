from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buku')
def buku():
    return render_template('buku.html')

@app.route('/pinjam')
def pinjam():
    return render_template('pinjam.html')

@app.route('/anggota')
def anggota():
    return render_template('anggota.html')

if __name__ == '__main__':
    app.run(debug=True)
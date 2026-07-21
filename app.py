from flask import Flask, render_template

app = Flask(__name__)

# Rute untuk halaman utama undangan
@app.route("/")
def index():
    # Ini akan membaca file index.html di dalam folder 'templates'
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


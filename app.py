from flask import Flask
app = Flask(__name__)

@app.route("/")
    def hello():
        return "Hello World!"

if __name__ == "__main__":
    app.run(app.config['0.0.0.0'], app.config['5000'])

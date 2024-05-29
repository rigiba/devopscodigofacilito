from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/ready")
def ready():
    return "<h1>!!Ready!</h1>"

@app.route("/api/avatar")
def avatar():
    return "<h1>Aca van los avatar</h1>"

@app.route("/api/avatar/spec")
def avatarspec():
     return render_template('avatar.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
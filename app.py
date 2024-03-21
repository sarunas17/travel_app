from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/main")
def main():
    return render_template("main.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/userprofile")
def userprofile():
    return render_template("userprofile.html")


@app.route("/404")
def page_not_found():
    return render_template("404.html")


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1')
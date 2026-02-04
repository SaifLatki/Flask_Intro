from flask import Flask,redirect, request,url_for,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# @app.route("/<name>")
# def user(name):
#     return f"Hello, {name}!"

# @app.route("/admin")
# def admin():
#     return redirect(url_for("admin", name="Admin"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        return redirect(url_for("user", usr=user))
    else:
       return render_template("login.html")
@app.route("/<usr>") 
def user(usr):
    return f"<h1>Hello, {usr}!</h1>"


if __name__ == "__main__":
    app.run( debug=True)
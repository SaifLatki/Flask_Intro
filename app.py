from flask import Flask,redirect, request,url_for,render_template,session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(days=5)

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
        session.permanent = True
        user = request.form["username"]
        session["username"] = user
        return redirect(url_for("user", usr=user))
    else:
       if "username" in session:
            return redirect(url_for("user"))
       return render_template("login.html")
@app.route("/user") 
def user():
    if "username" in session:
        usr = session["username"]
        return f"<h1>{usr}</h1>"
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run( debug=True)
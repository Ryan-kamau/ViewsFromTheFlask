from flask import Flask, render_template, request

app = Flask(__name__)

users = {}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    password = request.form["password"]

    if username in users:
        return "❌ User already exists! Try logging in."
    users[username] = password
    return f"✅ User {username} registered successfully!"

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if username in users and users[username] == password:
        return f"🎉 Welcome back, {username}!"
    return "❌ Invalid username or password!"

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/search")
def search():
    query = request.args.get("q")
    return render_template("search.html", query=query)

@app.route("/profile")
def profile():
    user_id = request.args.get("id")
    return render_template("profile.html", user_id=user_id)

if __name__ == "__main__":
    app.run(debug=True)

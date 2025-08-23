from flask import Flask, jsonify

app = Flask(_name_)

@app.route("/")
def home():
    return jsonify({"message": "AI Resume Job Matcher API is running 🚀"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


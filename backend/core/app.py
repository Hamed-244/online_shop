from flask import Flask , jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message" : "oh yes it work!"})

if __name__ == "__main__" :
    app.run(host="0.0.0.0" , port=8080 , debug=True)
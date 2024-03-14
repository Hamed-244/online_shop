from flask import Flask , jsonify
from admin.admin import admin_blueprint

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message" : "this is a sample e-commerce web application !"})

# app modules
app.register_blueprint(admin_blueprint)

if __name__ == "__main__" :
    app.run(host="0.0.0.0" , port=8080 , debug=True)
from flask import render_template, Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# @app.route('/slider_update', methods=['POST', 'GET'])
# def slider():
#     var = request.data
#     print(var)
#     return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
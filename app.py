from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cart", methods=["POST"])
def cart():
    data = request.get_json()
    total_price = sum(item["price"] * item["quantity"] for item in data["items"])
    # Здесь можно обработать заказ, сохранить его в базе данных и т. д.
    # ...
    return jsonify({"success": True, "total_price": total_price})

if __name__ == "__main__":
    app.run(debug=True)
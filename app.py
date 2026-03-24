from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database
items = {}

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Flask CI/CD CRUD API"}), 200


# CREATE
@app.route("/items", methods=["POST"])
def create_item():
    data = request.get_json()
    item_id = data.get("id")
    name = data.get("name")

    if not item_id or not name:
        return jsonify({"error": "id and name are required"}), 400

    if item_id in items:
        return jsonify({"error": "Item already exists"}), 409

    items[item_id] = {"id": item_id, "name": name}
    return jsonify(items[item_id]), 201


# READ ALL
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(list(items.values())), 200


# READ ONE
@app.route("/items/<item_id>", methods=["GET"])
def get_item(item_id):
    item = items.get(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item), 200


# UPDATE
@app.route("/items/<item_id>", methods=["PUT"])
def update_item(item_id):
    if item_id not in items:
        return jsonify({"error": "Item not found"}), 404

    data = request.get_json()
    name = data.get("name")

    if not name:
        return jsonify({"error": "name is required"}), 400

    items[item_id]["name"] = name
    return jsonify(items[item_id]), 200


# DELETE
@app.route("/items/<item_id>", methods=["DELETE"])
def delete_item(item_id):
    if item_id not in items:
        return jsonify({"error": "Item not found"}), 404

    deleted = items.pop(item_id)
    return jsonify({"deleted": deleted}), 200


# HEALTH CHECK
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "OK"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
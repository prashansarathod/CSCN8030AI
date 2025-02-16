from flask import Blueprint, request, jsonify
from data import database
from dev.models import predict_outcome

routes = Blueprint("routes", __name__)

@routes.route("/upload_animal", methods=["POST"])
def upload_animal():
    """API to upload animal data."""
    try:
        data = request.json
        insert_animal(data["name"], data["age"], data["breed"], data["health_status"], data["shelter_stay_days"], data["adoption_requests"])
        return jsonify({"message": "Animal data uploaded successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@routes.route("/get_animals", methods=["GET"])
def get_animals():
    """Fetch all stored animal records."""
    animals = database.fetch_all_animals()
    return jsonify({"animals": animals})

@routes.route("/predict", methods=["POST"])
def predict():
    """API to predict adoption outcomes."""
    try:
        data = request.json
        prediction = predict_outcome(data)
        return jsonify(prediction)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

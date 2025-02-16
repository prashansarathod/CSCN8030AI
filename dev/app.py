from flask import Flask
from flask_cors import CORS
from .routes import routes

app = Flask(__name__)
CORS(app)  # Allow Cross-Origin requests

# Register API routes
app.register_blueprint(routes)

@app.route("/")
def home():
    return "Paw Petrol API is running!"

if __name__ == "__main__":
    print("🚀 Starting Flask API on http://127.0.0.1:5000/")
    app.run(debug=True, port=5000)
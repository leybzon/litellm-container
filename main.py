import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from litellm import completion

# Load environment variables from .env file
load_dotenv()

# Flask app to handle API requests
app = Flask(__name__)

# Retrieve API keys from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

if not OPENAI_API_KEY or not ANTHROPIC_API_KEY:
    raise EnvironmentError("Both OPENAI_API_KEY and ANTHROPIC_API_KEY must be set as environment variables.")

# Endpoint to handle model inference requests
@app.route("/completion", methods=["POST"])
def handle_completion():
    try:
        # Parse the request payload
        data = request.json
        if not data:
            return jsonify({"error": "Invalid JSON payload"}), 400

        model = data.get("model")
        messages = data.get("messages")

        if not model or not messages:
            return jsonify({"error": "Both 'model' and 'messages' fields are required"}), 400

        # Set the appropriate API key based on the model
        if "openai" in model:
            os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
        elif "anthropic" in model:
            os.environ["ANTHROPIC_API_KEY"] = ANTHROPIC_API_KEY
        else:
            return jsonify({"error": f"Unsupported model '{model}'"}), 400

        # Call LiteLLM completion
        response = completion(model=model, messages=messages)

        # Ensure the response is serialized to JSON
        if hasattr(response, "dict"):
            return jsonify(response.dict())
        elif isinstance(response, dict):
            return jsonify(response)
        else:
            return jsonify({"error": "Response from LiteLLM is not serializable"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)


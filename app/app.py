import os
import logging
from flask import Flask, jsonify

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def home():
    logger.info("Home endpoint accessed")
    return jsonify({
        "status": "online",
        "message": "Welcome to the Automated Deploy Project API",
        "environment": os.getenv("ENV", "production")
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    # Use environment variables for configuration
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

from flask import Flask, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route('/api/datetime', methods=['GET'])
def get_datetime():
    """
    Get current date and time in JSON format.
    
    Returns:
        JSON response containing:
        - current_datetime: ISO formatted datetime string
        - timestamp: Unix timestamp
        - timezone: Timezone information
    """
    now = datetime.now(pytz.UTC)
    
    response_data = {
        "current_datetime": now.isoformat(),
        "timestamp": int(now.timestamp()),
        "timezone": "universal_coordinated_time",
        "local_datetime": datetime.now().isoformat(),
        "message": "Current date and time retrieved successfully"
    }
    
    return jsonify(response_data), 200


@app.route('/api/health', methods=['GET'])
def health_check():
    """
    Health check endpoint for the API.
    """
    return jsonify({
			"status": "ok",
			"message": "DateTime API is running",
			"timestamp": datetime.now().isoformat()
    }), 200


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
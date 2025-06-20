# DateTime API

This is a simple Python Flask API that provides current date and time information in JSON format.

## Features

- Get current date and time in ISO format
- Get Unix timestamp
- Includes both UTC and local time
- Health check endpoint
- Fully tested with unit tests

## API Endpoints

### 1. Get DateTime
**URL:\** `GET /api/datetime`

**Response Example:**
```json
{
  "current_datetime": "2025-06-20T09:30:15.789000+00:00",
  "timestamp": 1719043815,
  "timezone": "universal_coordinated_time",
  "local_datetime": "2025-06-20T09:30:15.789000",
  "message": "Current date and time retrieved successfully"
}
```

### 2. Health Check
**URL:** `GET /api/health`

**Response Example:**
```json
{
  "status": "ok",
  "message": "DateTime API is running",
  "timestamp": "2025-06-20T09:30:15.789000"
}
```

## Installation & Usage

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the API
```bash
python src/datetime_api.py
```

The API will be available at `http://localhost:5000`

### 3. Test the API
```bash
# Get current date and time
curl http://localhost:5000/api/datetime

# Health check
curl http://localhost:5000/api/health
```

### 4. Run Unit Tests
```bash
# Run all tests
python -m unittest discover tests

# Run specific test
python tests/test_datetime_api.py
```

## Project Structure
```
.
├── src/
│   └── datetime_api.py    # Main API application
├── tests/
│   └── test_datetime_api.py  # Unit tests
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## Dependencies

- **Flask*3*: Web framework for creating the API
- **pytz**: Timezone handling library

## Development

This API is built with simplicity and reliability in mind. It provides:

- Clean and simple API design
- Proper error handling
- Comprehensive test coverage
- Easy to deploy and scale
- Timezone aware date and time handling
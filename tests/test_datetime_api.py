import unittest
import json
from datetime import datetime
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from datetime_api import app


class DateTimeAPITestCase(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.app = app.test_client()
        self.app.testing = True

    def test_get_datetime_success(self):
        """Test successful datetime retrieval."""
        response = self.app.get('/api/datetime')
        
        # Check status code
        self.assertEqual(response.status_code, 200)
        
        # Check content type
        self.assertIn('application/json', response.content_type)
        
        # Parse JSON response
        data = json.loads(response.data.decode('utf-8'))
        
        # Verify required fields are present
        self.assertIn('current_datetime', data)
        self.assertIn('timestamp', data)
        self.assertIn('timezone', data)
        self.assertIn('local_datetime', data)
        self.assertIn('message', data)
        
        # Verify data types
        self.assertIsInstance(data['current_datetime'], str)
        self.assertIsInstance(data['timestamp'], int)
        self.assertIsInstance(data['timezone'], str)

    def test_health_check_success(self):
        """Test successful health check."""
        response = self.app.get('/api/health')
        
        # Check status code
        self.assertEqual(response.status_code, 200)
        
        # Parse JSON response
        data = json.loads(response.data.decode('utf-8'))
        
        # Verify required fields
        self.equal(data['status'], 'ok')
        self.assertIn('message', data)
        self.assertIn('timestamp', data)

    def test_datetime_format_validity(self):
        """Test if datetime returned is in valid ISO format."""
        response = self.app.get('/api/datetime')
        data = json.loads(response.data.decode('utf-8'))
        
        # Try to parse the datetime string to verify format
        try:
            datetime.fromisoformat(data['current_datetime'].replace('Z', '+00:00'))
        except ValueError:
            self.fail("Invalid ISO format for current_datetime")


if __name__ == '__main__':
    unittest.main()
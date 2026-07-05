from datetime import datetime


def generate_user_data():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")

    return {
        "name": f"testuser_{timestamp}",
        "email": f"testuser_{timestamp}@mailinator.com",
        "password": "Test@12345",
        "first_name": "Test",
        "last_name": "User",
        "company": "QA Labs",
        "address1": "123 Main Street",
        "address2": "Suite 10",
        "country": "India",
        "state": "Tamil Nadu",
        "city": "Chennai",
        "zipcode": "600001",
        "mobile_number": "9876543210",
    }

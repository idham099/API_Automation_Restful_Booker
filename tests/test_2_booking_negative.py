import pytest
import requests
import json
import allure

@allure.title("Negative: #1 POST - Payload Tidak Lengkap")
@allure.tag("Negative", "Validation")
def test_post_invalid_payload_fails(base_url):
    invalid_payload = {
        "lastname": "NegativeTest",
        "totalprice": 500,
        "depositpaid": True,
        "bookingdates": {"checkin": "2025-12-20", "checkout": "2025-12-25"},
        "additionalneeds": "Air Minum"
    }

    with allure.step("1. Mencoba POST dengan payload tidak lengkap"):
        endpoint = f"{base_url}/booking"

        allure.attach( json.dumps(invalid_payload, indent=4),  name="Request Payload (Missing 'firstname')", attachment_type=allure.attachment_type.JSON)

        response = requests.post(
            endpoint, 
            headers={"Content-Type": "application/json"}, 
            json=invalid_payload
        )

        allure.attach(f"Status Code: {response.status_code}\nBody: {response.text}", name="Response Error (Expected 500)", attachment_type=allure.attachment_type.TEXT)
        
        assert response.status_code == 500, \
            f"Expected 500, but received {response.status_code}"
        



@allure.title("Negative: #2 DELETE - Tanpa Token Otentikasi")
@allure.tag("Negative", "Security")
def test_delete_unauthorized_fails(base_url, created_booking_id):
    
    booking_id = created_booking_id
    endpoint = f"{base_url}/booking/{booking_id}"
    empty_headers = {"Content-Type": "application/json"}
    
    with allure.step(f"2. Mencoba DELETE Booking ID {booking_id} tanpa Token"):
        allure.attach(
            json.dumps(empty_headers, indent=4), 
            name="Request Headers (Missing Cookie/Token)", 
            attachment_type=allure.attachment_type.JSON
        )
        
        response = requests.delete(
            endpoint, 
            headers=empty_headers 
        )

        allure.attach(
            f"Status Code: {response.status_code}\nBody: {response.text}",
            name="Response Error (Expected 403 Forbidden)",
            attachment_type=allure.attachment_type.TEXT
        )
        
        # Verifikasi Status 403 Forbidden
        assert response.status_code == 403, \
            f"Expected 403, but received {response.status_code}"
        
        # Verifikasi body
        assert response.text == "Forbidden"



@allure.title("Negative: #3 GET - ID Tidak Ada")
@allure.tag("Negative", "Integrity")
def test_get_non_existent_id_fails(base_url):
    
    non_existent_id = 99999999 
    
    with allure.step(f"3. Mencoba GET Booking ID: {non_existent_id}"):
        endpoint = f"{base_url}/booking/{non_existent_id}"
        
        response = requests.get(endpoint)

        allure.attach(
            f"URL: {endpoint}", 
            name="Request URL", 
            attachment_type=allure.attachment_type.TEXT
        )

        allure.attach(
            f"Status Code: {response.status_code}\nBody: {response.text}",
            name="Response Error (Expected 404 Not Found)",
            attachment_type=allure.attachment_type.TEXT
        )
        
        # Verifikasi Status 404 Not Found
        assert response.status_code == 404, \
            f"Expected 404, but received {response.status_code}"
        
        # Verifikasi body
        assert response.text == "Not Found"
import pytest
import datetime
from dotenv import load_dotenv
import os
import requests

load_dotenv()

#1. Edit fixture untuk base url
@pytest.fixture(scope="session")
def base_url():
   return " https://restful-booker.herokuapp.com/"

@pytest.fixture(scope="session")
def auth_token(base_url):
    username = os.getenv("BOOKER_USERNAME")
    password = os.getenv("BOOKER_PASSWORD")
    print(f"\n[DEBUG LOGIN] Username yang digunakan: {username}")
    print(f"[DEBUG LOGIN] Password yang digunakan: {password}")
    
    endpoint = f"{base_url}/auth"
    payload = {
        "username": username,
        "password": password
    }

    response = requests.post(endpoint, json=payload)
    if response.status_code != 200:
        raise Exception(f"Gagal login. Status: {response.status_code}")

    token = response.json().get("token")
    if not token:
        raise Exception("Token tidak ditemukan dalam respons login.")

    return token



#2. Edit fixture untuk header http 
@pytest.fixture(scope="session")
def api_header(auth_token):
   return {
      "Content-Type": "application/json",
      "Cookie": f"token={auth_token}"
   }


#3.membuat booking baru (POST /booking)
@pytest.fixture(scope="module")
def create_booking_payload():
    today = datetime.date.today().strftime('%Y-%m-%d')
    check_out_date = (datetime.date.today() + datetime.timedelta(days=5)).strftime('%Y-%m-%d')
    
    payload = {
        "firstname": "Aldi",
        "lastname": "Sembiring",
        "totalprice": 1500,
        "depositpaid": True,
        "bookingdates": {
            "checkin": today,          
            "checkout": check_out_date 
        },
        "additionalneeds": "Wi-Fi dan sarapan"
    }
   
    return payload


#4. membuat booking dan memberikan ID (POST)
@pytest.fixture(scope="module")
def created_booking_id(base_url, api_header, create_booking_payload):
    post_endpoint = f"{base_url}/booking"
    post_response = requests.post(post_endpoint,headers={"Content-Type": "application/json"},json=create_booking_payload)
    if post_response.status_code != 200:
        raise Exception(f"Fixture Gagal membuat booking. Status: {post_response.status_code}")
        
    booking_id = post_response.json().get("bookingid")
    yield booking_id 



#5. operasi PUT/PATCH (Update)
@pytest.fixture
def update_booking_payload():
    return {
        "firstname": "Adi",           
        "lastname": "Santoso",        
        "totalprice": 9999,           
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-01-01",  
            "checkout": "2026-01-10"
        },
        "additionalneeds": "Premium Suite & Spa"
    }


#6. Partial Update Booking (PATCH)
@pytest.fixture
def partial_update_payload():
    return {
        "firstname": "Rudy Tabuti",          
        "additionalneeds": "Hanya Cokelat Panas" 
    }

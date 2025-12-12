import pytest
import requests
import json
import allure


# 1. new booking (POST)
@allure.title("Positive : #1 Memmbuat new booking (POST)")
@allure.tag("CRUD", "POST")
def test_post_new_booking(base_url, api_header, create_booking_payload):
    with allure.step("1. Memmbuat new booking (POST)"):
        endpoint = f"{base_url}/booking"

        #evidence sebelum
        allure.attach(json.dumps(create_booking_payload, indent=4),  name="Request Payload", attachment_type=allure.attachment_type.JSON)

        response = requests.post(endpoint, headers={"Content-Type": "application/json"}, json=create_booking_payload)

        allure.attach(f"Status Code: {response.status_code}\nHeaders: {response.headers}", name="Response Metadata", attachment_type=allure.attachment_type.TEXT)
        allure.attach( response.text, name="Response Body (Success)", attachment_type=allure.attachment_type.JSON)
        
        # Verifikasi status 200
        assert response.status_code == 200
        
        # Verifikasi data yang dibuat
        databook = response.json()
        print(databook)
        #print("=====")
        created_firstname = response.json()["booking"]["firstname"]
        assert created_firstname == "Aldi"

    

#2. Menampilkan list semua daftar Booking
@allure.title("Positive : #2 Membaca Booking List (GET)")
@allure.tag("CRUD", "GET")
def test_get_bookingList(base_url, api_header):
    with allure.step("2. Membaca Booking List (GET)"):            
        endpoint = f"{base_url}/booking"
        response = requests.get(endpoint, headers=api_header)
        
        # Verifikasi Status 200 OK
        assert response.status_code == 200
        allure.attach(f"Status Code: {response.status_code}\nHeaders: {response.headers}", name="Response Metadata", attachment_type=allure.attachment_type.TEXT)

        # Verifikasi Data 
        data = response.json()
        allure.attach(json.dumps(data, indent=4), name="Booking List IDs", attachment_type=allure.attachment_type.JSON)
        #print(data)
        #print("=====")
        assert isinstance(data, list)
        assert len(data) >= 1



#3. Menampilkan daftar booking berdasarkan Id
@allure.title("Positive : #3 Membaca Booking ID (GET)")
@allure.tag("CRUD", "GET")
def test_get_bookingId(base_url, api_header, created_booking_id):
    booking_id = created_booking_id 
    
    with allure.step(f"3. Membaca Booking ID: {booking_id} (GET)"): 
        endpoint = f"{base_url}/booking/{booking_id}"
        response = requests.get(endpoint, headers=api_header) 
        
        # Verifikasi Status 200 OK
        assert response.status_code == 200
        allure.attach(f"Status Code: {response.status_code}\nHeaders: {response.headers}", name="Response Metadata", attachment_type=allure.attachment_type.TEXT)


        # Verifikasi Data 
        dataId = response.json()
        allure.attach( json.dumps(dataId, indent=4),  name=f"Booking Data ID {booking_id} Found",  attachment_type=allure.attachment_type.JSON)
        #print(dataId) 
        #print("===")
        assert isinstance(dataId, dict)
        assert dataId["bookingdates"] is not None 
        assert dataId["firstname"] == "Aldi"



#4. Menampilkan daftar ping - healthcheck
@allure.title("Positive : #4 Membaca daftar ping - healthcheck (GET)")
@allure.tag("CRUD", "GET")
def test_get_healthCheck(base_url, api_header):
    with allure.step(f"4. Membaca daftar ping - healthcheck (GET)"):      
        endpoint = f"{base_url}/ping"
        response = requests.get(endpoint, headers=api_header)
        allure.attach(f"Status Code: {response.status_code}\nHeaders: {response.headers}", name="Response Metadata", attachment_type=allure.attachment_type.TEXT)
        allure.attach(response.text, name="Response Body (Expected 'Created')", attachment_type=allure.attachment_type.TEXT)
        # Verifikasi Status 201 OK
        assert response.status_code == 201, f"Health Check Gagal. Status diterima: {response.status_code}"

        # Verifikasi Data 
        assert response.text == "Created", f"Body respons tidak sesuai. Diharapkan 'Created', diterima: {response.text}"
        #print(response.status_code, response.text  )
        #print ("===")



#5. operasi PUT/PATCH (Update)
@allure.title("Positive : #5 Update Booking Penuh (PUT)")
@allure.tag("CRUD", "Update")
def test_update_booking_success(base_url, api_header, created_booking_id, update_booking_payload):
    booking_id = created_booking_id
    
    with allure.step(f"5.1. Memperbarui Booking ID {booking_id} dengan PUT"):
        endpoint = f"{base_url}/booking/{booking_id}"

        allure.attach(json.dumps(update_booking_payload, indent=4), name="Request Payload (PUT)", attachment_type=allure.attachment_type.JSON)

        response = requests.put(endpoint,headers=api_header,json=update_booking_payload)

        # Verifikasi Status 200 OK
        assert response.status_code == 200, f"Update PUT gagal. Status: {response.status_code}, Body: {response.text}"
        
         # Verifikasi data
    with allure.step("5.2. Verifikasi Data Baru"):
        updated_data = response.json()
        assert updated_data["firstname"] == "Adi"
        assert updated_data["totalprice"] == 9999
        assert updated_data["additionalneeds"] == "Premium Suite & Spa"

        allure.attach(json.dumps(updated_data, indent=4),  name="Updated Booking Data", attachment_type=allure.attachment_type.JSON)
        #print(updated_data)
        #print("===")



#6. Partial Update Booking (PATCH)
@allure.title("Positive : #6 Partial Update Booking (PATCH)")
@allure.tag("CRUD", "PartialUpdate")
def test_partial_update_booking_success(base_url, api_header, created_booking_id, partial_update_payload):
      
    booking_id = created_booking_id
    
    with allure.step(f"6.1. Memperbarui Booking ID {booking_id} sebagian (PATCH)"):
        endpoint = f"{base_url}/booking/{booking_id}"
        response = requests.patch(endpoint, headers=api_header, json=partial_update_payload)

        # Verifikasi Status 200 OK
        assert response.status_code == 200, f"Update PATCH gagal. Status: {response.status_code}, Body: {response.text}"
        
        # Verifikasi data
    with allure.step("6.2. Verifikasi Data yang Diubah"):
        updated_data_patch = response.json()
        
        # Verifikasi 1: Nama depan sudah berubah sesuai payload PATCH
        assert updated_data_patch["firstname"] == "Rudy Tabuti"
        assert updated_data_patch["additionalneeds"] == "Hanya Cokelat Panas"
        assert updated_data_patch["totalprice"] == 9999
        #print(updated_data_patch)
        #print("===")
        
        # Lampirkan respons ke laporan Allure
        allure.attach(json.dumps(updated_data_patch, indent=4), name="Partial Updated Booking Data", attachment_type=allure.attachment_type.JSON
        )



#7.  Menguji penghapusan booking. (Delete) 
@allure.title("Positive : #7 Delete Booking Sukses")
@allure.tag("CRUD", "Delete")
def test_delete_booking_success(base_url, api_header, created_booking_id):

    booking_id_to_delete = created_booking_id 

    endpoint = f"{base_url}/booking/{booking_id_to_delete}"
    
    with allure.step(f"7.1. Menghapus Booking ID: {booking_id_to_delete} (DELETE)"):
        delete_response = requests.delete(endpoint,headers=api_header)
        
        # Verifikasi Status 200 , tapi default 201 Created atau 204 No Content
        assert delete_response.status_code == 201, \
            f"Gagal menghapus booking. Status diterima: {delete_response.status_code}, Body: {delete_response.text}"
        assert delete_response.text == "Created"
        #print(delete_response.status_code, delete_response.text)
        #print("===")


    with allure.step("7.2. Verifikasi penghapusan dengan mencoba GET ID yang sama"):
        get_response = requests.get(endpoint)
        
        # Verifikasi Status 404 Not Found
        assert get_response.status_code == 404, \
            f"Verifikasi Gagal. Booking masih ditemukan (Status: {get_response.status_code})"
        
        allure.attach(f"Status Code: {get_response.status_code}\nText: {get_response.text}", name="Verification GET Response (Expected 404)", attachment_type=allure.attachment_type.TEXT)

        assert get_response.text == "Not Found"
        
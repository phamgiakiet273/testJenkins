import pytest
import requests

BASE_URL = "http://localhost:5000"

def test_get_version():
    response = requests.get(f"{BASE_URL}/get_version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}

def test_check_prime_missing_param():
    response = requests.get(f"{BASE_URL}/check_prime")
    assert response.status_code == 400
    assert "error" in response.json()

def test_check_prime_negative():
    response = requests.get(f"{BASE_URL}/check_prime", params={"number": -1})
    assert response.status_code == 200
    assert not response.json()["is_prime"]

def test_check_prime_zero():
    response = requests.get(f"{BASE_URL}/check_prime", params={"number": 0})
    assert response.status_code == 200
    assert not response.json()["is_prime"]

def test_check_prime_one():
    response = requests.get(f"{BASE_URL}/check_prime", params={"number": 1})
    assert response.status_code == 200
    assert not response.json()["is_prime"]

def test_check_prime_two():
    response = requests.get(f"{BASE_URL}/check_prime", params={"number": 2})
    assert response.status_code == 200
    assert response.json()["is_prime"]

def test_check_prime_three():
    response = requests.get(f"{BASE_URL}/check_prime", params={"number": 3})
    assert response.status_code == 200
    assert response.json()["is_prime"]

def test_check_prime_four():
    response = requests.get(f"{BASE_URL}/check_prime", params={"number": 4})
    assert response.status_code == 200
    assert not response.json()["is_prime"]

def test_check_prime_large_prime():
    response = requests.get(f"{BASE_URL}/check_prime", params={"number": 29})
    assert response.status_code == 200
    assert response.json()["is_prime"]

def test_check_prime_large_non_prime():
    response = requests.get(f"{BASE_URL}/check_prime", params={"number": 30})
    assert response.status_code == 200
    assert not response.json()["is_prime"]

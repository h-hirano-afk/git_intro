# tests/test_api.py
import json
import pytest
from fastapi.testclient import TestClient
import app
client = TestClient(app)
# JSONファイルからテストケースを読み込む関数
def load_test_cases(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)["test_cases"]
@pytest.mark.parametrize("test_case", load_test_cases("test_cases.json"))
def test_read_details(test_case):
    input_data = test_case["input"]
    expected_output = test_case["expected"]
  
    response = client.get("/fsportal_dev_apistage/detail", params=input_data)
  
    assert response.status_code == 200
    assert response.json() == expected_output
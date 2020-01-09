import requests
import json

def test_post_headers_body_json():
    url = 'http://localhost:8000/customers'
    
    # Additional headers.
    headers = {'Content-Type': 'application/json' } 

    # Body
    # payload = {'key1': 1, 'key2': 'value2'}
    
    # convert dict to json by json.dumps() for body data. 
    # data=json.dumps(payload,indent=4)
    resp = requests.post(url)       
    
    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 200
    resp_body = resp.json()
    # assert resp_body['url'] == url
    
    # print response full body as text
    print(resp.text)

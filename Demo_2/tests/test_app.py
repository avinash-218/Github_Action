from ..app import app

def test_hello_world():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data == b"Hello World !"

def test_health():
    response = app.test_client().get('/health')

    assert response.status_code == 200
    assert response.data == b"API Active"
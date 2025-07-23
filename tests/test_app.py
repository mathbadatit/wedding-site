from myapp import create_app

def test_home_status_code():
    myapp = create_app()
    client = myapp.test_client()
    response = client.get('/')
    assert response.status_code == 200

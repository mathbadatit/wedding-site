from flask import Flask

def test_flask_runs():
    myapp = Flask(__name__)

    @myapp.route('/')
    def home():
        return 'Hello Flask!'

    client = myapp.test_client()
    response = client.get('/')
    assert response.data == b'Hello Flask!'

def test_post_seating_no_auth(client):
    assert client.get('/seat/reserved', data={'show_id': '1', 'seat_id': '1'}).status_code == 401


from flask_jwt_extended.utils import create_access_token
from app import app


def get_header():
    with app.app_context():
        access_toke = create_access_token('testuser')

    return {
        'Authorization': 'Bearer {}'.format(access_toke)
    }


def test_get_seating_authorized(client):
    assert client.get('/seat/reserved',
                      headers=get_header(),
                      data={'show_id': '1', 'seat_id': '1'}).status_code == 200

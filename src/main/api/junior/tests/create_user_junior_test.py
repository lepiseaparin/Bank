import requests
import pytest


@pytest.mark.junior_api
class TestCreateUser:
    def test_create_user(self):
        login_admin_response = requests.post(
            url="http://localhost:4111/api/auth/token/login",
            json={
                "username": "admin",
                "password": "123456"
            },
            headers={
                "Content-Type": "application/json",
                "accept": "application/json"
            }
        )

        assert login_admin_response.status_code == 200
        token = login_admin_response.json().get("token")

        create_user_response = requests.post(
            url="http://localhost:4111/api/admin/create",
            json={
              "username": "Kuner5",
              "password": "Pas!sw0rd",
              "role": "ROLE_USER"
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}"
            }
        )

        assert create_user_response.status_code == 200
        assert create_user_response.json().get("username") == "Kuner5"
        assert create_user_response.json().get("role") == "ROLE_USER"

    @pytest.mark.parametrize(
        "username, password",
        [
            ("хуй", "Pas!sw0rd" ),
            ("ab", "Pas!sw0rd"),
            ("abc!", "Pas!sw0rd"),
            ("Kuner14", "Pas!sw0rд"),
            ("Kuner15", "Passw!9"),
            ("Kuner16", "passw!o9d"),
            ("Kuner17", "PASSWO!O9D"),
            ("Kuner18", "PASSWo9Dd"),
            ("Kuner19", "PASSWWo!Dd"),
        ]
    )
    def test_create_user_invalid(self, username, password):
        login_admin_response = requests.post(
            url="http://localhost:4111/api/auth/token/login",
            json={
                "username": "admin",
                "password": "123456"
            },
            headers={
                "Content-Type": "application/json",
                "accept": "application/json"
            }
        )

        assert login_admin_response.status_code == 200
        token = login_admin_response.json().get("token")

        create_user_response = requests.post(
            url="http://localhost:4111/api/admin/create",
            json={
                "username": username,
                "password": password,
                "role": "ROLE_USER"
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}"
            }
        )

        assert create_user_response.status_code == 400
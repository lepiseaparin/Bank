import requests
import pytest

@pytest.mark.junior_api
class TestCreateCreditUser:
    def test_login_admin(self):
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


        create_users1_response = requests.post(
            url="http://localhost:4111/api/admin/create",
            json={
              "username": "Kuneringo7",
              "password": "Pas!sw0rd",
              "role": "ROLE_CREDIT_SECRET"
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}"
            }
        )

        assert create_users1_response.status_code == 200
        assert create_users1_response.json().get("username") == "Kuneringo7"
        assert create_users1_response.json().get("role") == "ROLE_CREDIT_SECRET"


        login_user_response = requests.post(
            url="http://localhost:4111/api/auth/token/login",
            json={
                "username": "Kuneringo7",
                "password": "Pas!sw0rd"
            },
            headers={
                "Content-Type": "application/json",
                "accept": "application/json"
            }
        )

        assert login_user_response.status_code == 200
        token = login_user_response.json().get("token")


        create_account_response = requests.post(
            url="http://localhost:4111/api/account/create",
            headers={
                "accept": "application/json",
                "Authorization": f"Bearer {token}"
            }
        )

        assert create_account_response.status_code == 201
        assert create_account_response.json().get("balance") == 0
        account_id = create_account_response.json().get("id")

        credit_user_response = requests.post(
            url="http://localhost:4111/api/credit/request",
            json={
                "accountId": account_id,
                "amount": 5000,
                "termMonths": 12
            },
            headers={
                "Content-Type": "application/json",
                "accept": "application/json",
                "Authorization": f"Bearer {token}"
            }
        )

        assert credit_user_response.status_code == 201
        assert credit_user_response.json().get("balance") == 5000

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

        create_user1_response = requests.post(
            url="http://localhost:4111/api/admin/create",
            json={
                "username": "Kuneringo13",
                "password": "Pas!sw0rd",
                "role": "ROLE_USER"
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}"
            }
        )

        assert create_user1_response.status_code == 200
        assert create_user1_response.json().get("username") == "Kuneringo13"
        assert create_user1_response.json().get("role") == "ROLE_USER"

        create_user2_response = requests.post(
            url="http://localhost:4111/api/admin/create",
            json={
                "username": "Kuneringo14",
                "password": "Pas!sw0rd",
                "role": "ROLE_CREDIT_SECRET"
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}"
            }
        )

        assert create_user2_response.status_code == 200
        assert create_user2_response.json().get("username") == "Kuneringo14"
        assert create_user2_response.json().get("role") == "ROLE_CREDIT_SECRET"

        create_user3_response = requests.post(
            url="http://localhost:4111/api/admin/create",
            json={
                "username": "Kuneringo15",
                "password": "Pas!sw0rd",
                "role": "ROLE_CREDIT_SECRET"
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}"
            }
        )

        assert create_user3_response.status_code == 200
        assert create_user3_response.json().get("username") == "Kuneringo15"
        assert create_user3_response.json().get("role") == "ROLE_CREDIT_SECRET"

    @pytest.mark.parametrize(
        "username, password, amount",
        [
            ("Kuneringo14", "Pas!sw0rd", 4999),
            ("Kuneringo15", "Pas!sw0rd", 15001),
        ]
    )
    def test_invalid_credit(self, username, password, amount):
        login_user_response = requests.post(
            url="http://localhost:4111/api/auth/token/login",
            json={
                "username": username,
                "password": password
            },
            headers={
                "Content-Type": "application/json",
                "accept": "application/json"
            }
        )

        assert login_user_response.status_code == 200
        token = login_user_response.json().get("token")


        create_account_response = requests.post(
            url="http://localhost:4111/api/account/create",
            headers={
                "accept": "application/json",
                "Authorization": f"Bearer {token}"
            }
        )

        assert create_account_response.status_code == 201
        assert create_account_response.json().get("balance") == 0
        account_id = create_account_response.json().get("id")

        credit_user_response = requests.post(
            url="http://localhost:4111/api/credit/request",
            json={
                "accountId": account_id,
                "amount": amount,
                "termMonths": 12
            },
            headers={
                "Content-Type": "application/json",
                "accept": "application/json",
                "Authorization": f"Bearer {token}"
            }
        )

        assert credit_user_response.status_code == 400

    @pytest.mark.parametrize(
        "username, password, amount",
        [
            ("Kuneringo13", "Pas!sw0rd", 4999),
            ("admin", "123456", 15001),
        ]
    )
    def invalid_role_credit(self, username, password, amount):
        login_user_response = requests.post(
            url="http://localhost:4111/api/auth/token/login",
            json={
                "username": username,
                "password": password
            },
            headers={
                "Content-Type": "application/json",
                "accept": "application/json"
            }
        )

        assert login_user_response.status_code == 200
        token = login_user_response.json().get("token")


        create_account_response = requests.post(
            url="http://localhost:4111/api/account/create",
            headers={
                "accept": "application/json",
                "Authorization": f"Bearer {token}"
            }
        )

        assert create_account_response.status_code == 201
        assert create_account_response.json().get("balance") == 0
        account_id = create_account_response.json().get("id")

        credit_user_response = requests.post(
            url="http://localhost:4111/api/credit/request",
            json={
                "accountId": account_id,
                "amount": amount,
                "termMonths": 12
            },
            headers={
                "Content-Type": "application/json",
                "accept": "application/json",
                "Authorization": f"Bearer {token}"
            }
        )

        assert credit_user_response.status_code == 403







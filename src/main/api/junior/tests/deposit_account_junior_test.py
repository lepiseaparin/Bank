import requests
import pytest

@pytest.mark.junior_api
class TestCreateDepositAccount:
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
              "username": "Kuneringo200",
              "password": "Pas!sw0rd",
              "role": "ROLE_USER"
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}"
            }
        )

        assert create_users1_response.status_code == 200
        assert create_users1_response.json().get("username") == "Kuneringo200"
        assert create_users1_response.json().get("role") == "ROLE_USER"


        login_user_response = requests.post(
            url="http://localhost:4111/api/auth/token/login",
            json={
                "username": "Kuneringo200",
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


        deposit_user_response = requests.post(
            url="http://localhost:4111/api/account/deposit",
            json={
                "accountId": account_id,
                "amount": 1000
            },
            headers={
                "accept": "application/json",
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            }
        )

        assert deposit_user_response.status_code == 200
        assert deposit_user_response.json().get("balance") == 1000


    def test_login_user(self):
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
                "username": "Kuneringo201",
                "password": "Pas!sw0rd",
                "role": "ROLE_USER"
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}"
            }
        )

        assert create_users1_response.status_code == 200
        assert create_users1_response.json().get("username") == "Kuneringo201"
        assert create_users1_response.json().get("role") == "ROLE_USER"

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
                "username": "Kuneringo221",
                "password": "Pas!sw0rd",
                "role": "ROLE_USER"
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}"
            }
        )

        assert create_users1_response.status_code == 200
        assert create_users1_response.json().get("username") == "Kuneringo221"
        assert create_users1_response.json().get("role") == "ROLE_USER"


    @pytest.mark.parametrize(
        "login, deposit",
        [
            ("Kuneringo201", 999),
            ("Kuneringo221",9001)
        ]
    )
    def test_invalid_deposit(self, login,deposit):
        login_user_response = requests.post(
            url="http://localhost:4111/api/auth/token/login",
            json={
                "username": login,
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


        deposit_user_response = requests.post(
            url="http://localhost:4111/api/account/deposit",
            json={
                "accountId": account_id,
                "amount": deposit
            },
            headers={
                "accept": "application/json",
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            }
        )
        assert deposit_user_response.status_code == 400








import requests
import pytest

@pytest.mark.junior_api
class TestRepayCreditUser:
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
              "username": "Kuneringo8",
              "password": "Pas!sw0rd",
              "role": "ROLE_CREDIT_SECRET"
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}"
            }
        )

        assert create_users1_response.status_code == 200
        assert create_users1_response.json().get("username") == "Kuneringo8"
        assert create_users1_response.json().get("role") == "ROLE_CREDIT_SECRET"


        login_user_response = requests.post(
            url="http://localhost:4111/api/auth/token/login",
            json={
                "username": "Kuneringo8",
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
        credit_id = credit_user_response.json().get("creditId")

        repay_credit_response = requests.post(
            url="http://localhost:4111/api/credit/repay",
            json={
                "creditId": credit_id,
                "accountId": account_id,
                "amount": 5000,
            },
            headers={
                "Content-Type": "application/json",
                "accept": "application/json",
                "Authorization": f"Bearer {token}"
            }
        )

        assert repay_credit_response.status_code == 200
        assert repay_credit_response.json().get("amountDeposited") == 5000



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
                "username": "Kuneringo16",
                "password": "Pas!sw0rd",
                "role": "ROLE_CREDIT_SECRET"
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}"
            }
        )

        assert create_user1_response.status_code == 200
        assert create_user1_response.json().get("username") == "Kuneringo16"
        assert create_user1_response.json().get("role") == "ROLE_CREDIT_SECRET"

        create_user2_response = requests.post(
            url="http://localhost:4111/api/admin/create",
            json={
                "username": "Kuneringo17",
                "password": "Pas!sw0rd",
                "role": "ROLE_CREDIT_SECRET"
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}"
            }
        )

        assert create_user2_response.status_code == 200
        assert create_user2_response.json().get("username") == "Kuneringo17"
        assert create_user2_response.json().get("role") == "ROLE_CREDIT_SECRET"



    @pytest.mark.parametrize(
        "username, password, amount",
        [
            ("Kuneringo16", "Pas!sw0rd", 4999),
            ("Kuneringo17", "Pas!sw0rd", 15001),
        ]
    )
    def test_invalid_repay_credit(self, username, password, amount):
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
        credit_id = credit_user_response.json().get("creditId")

        repay_credit_response = requests.post(
            url="http://localhost:4111/api/credit/repay",
            json={
                "creditId": credit_id,
                "accountId": account_id,
                "amount": amount,
            },
            headers={
                "Content-Type": "application/json",
                "accept": "application/json",
                "Authorization": f"Bearer {token}"
            }
        )

        assert repay_credit_response.status_code == 422






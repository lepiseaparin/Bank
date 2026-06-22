import requests
import pytest



@pytest.mark.junior_api
class TestTransferAccount:
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

        create_user1_response = requests.post(
            url="http://localhost:4111/api/admin/create",
            json={
                "username": "Kuneringo5",
                "password": "Pas!sw0rd",
                "role": "ROLE_USER"
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}"
            }
        )

        assert create_user1_response.status_code == 200
        assert create_user1_response.json().get("username") == "Kuneringo5"
        assert create_user1_response.json().get("role") == "ROLE_USER"

        create_user2_response = requests.post(
            url="http://localhost:4111/api/admin/create",
            json={
                "username": "Kuneringo6",
                "password": "Pas!sw0rd",
                "role": "ROLE_USER"
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}"
            }
        )

        assert create_user2_response.status_code == 200
        assert create_user2_response.json().get("username") == "Kuneringo6"
        assert create_user2_response.json().get("role") == "ROLE_USER"

        login_user1_response = requests.post(
            url="http://localhost:4111/api/auth/token/login",
            json={
                "username": "Kuneringo5",
                "password": "Pas!sw0rd"
            },
            headers={
                "Content-Type": "application/json",
                "accept": "application/json"
            }
        )

        assert login_user1_response.status_code == 200
        token_user1 = login_user1_response.json().get("token")

        create_account_user1_response = requests.post(
            url="http://localhost:4111/api/account/create",
            headers={
                "accept": "application/json",
                "Authorization": f"Bearer {token_user1}"
            }
        )

        assert create_account_user1_response.status_code == 201
        assert create_account_user1_response.json().get("balance") == 0
        account_user1_id = create_account_user1_response.json().get("id")

        deposit_user1_response = requests.post(
            url="http://localhost:4111/api/account/deposit",
            json={
                "accountId": account_user1_id,
                "amount": 1000
            },
            headers={
                "accept": "application/json",
                "Authorization": f"Bearer {token_user1}",
                "Content-Type": "application/json"
            }
        )

        assert deposit_user1_response.status_code == 200
        assert deposit_user1_response.json().get("balance") == 1000

        login_user2_response = requests.post(
            url="http://localhost:4111/api/auth/token/login",
            json={
                "username": "Kuneringo6",
                "password": "Pas!sw0rd"
            },
            headers={
                "Content-Type": "application/json",
                "accept": "application/json"
            }
        )

        assert login_user2_response.status_code == 200
        token_user2 = login_user1_response.json().get("token")

        create_account_user2_response = requests.post(
            url="http://localhost:4111/api/account/create",
            headers={
                "accept": "application/json",
                "Authorization": f"Bearer {token_user2}"
            }
        )

        assert create_account_user2_response.status_code == 201
        assert create_account_user2_response.json().get("balance") == 0
        account_user2_id = create_account_user2_response.json().get("id")

        transfer_user2_response = requests.post(
            url="http://localhost:4111/api/account/transfer",
            json={
                "fromAccountId": account_user1_id,
                "toAccountId": account_user2_id,
                "amount": 600
            },
            headers={
                "Content-Type": "application/json",
                "accept": "application/json",
                "Authorization": f"Bearer {token_user1}"
            }
        )

        assert transfer_user2_response.status_code == 200
        assert transfer_user2_response.json().get("fromAccountIdBalance") == 400


    def test_create_users(self):
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
              "username": "Kuneringo9",
              "password": "Pas!sw0rd",
              "role": "ROLE_USER"
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}"
            }
        )

        assert create_user1_response.status_code == 200
        assert create_user1_response.json().get("username") == "Kuneringo9"
        assert create_user1_response.json().get("role") == "ROLE_USER"


        create_user2_response = requests.post(
            url="http://localhost:4111/api/admin/create",
            json={
              "username": "Kuneringo10",
              "password": "Pas!sw0rd",
              "role": "ROLE_USER"
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}"
            }
        )

        assert create_user2_response.status_code == 200
        assert create_user2_response.json().get("username") == "Kuneringo10"
        assert create_user2_response.json().get("role") == "ROLE_USER"


        create_user3_response = requests.post(
            url="http://localhost:4111/api/admin/create",
            json={
              "username": "Kuneringo11",
              "password": "Pas!sw0rd",
              "role": "ROLE_USER"
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}"
            }
        )

        assert create_user3_response.status_code == 200
        assert create_user3_response.json().get("username") == "Kuneringo11"
        assert create_user3_response.json().get("role") == "ROLE_USER"


        create_user4_response = requests.post(
            url="http://localhost:4111/api/admin/create",
            json={
              "username": "Kuneringo12",
              "password": "Pas!sw0rd",
              "role": "ROLE_USER"
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}"
            }
        )

        assert create_user4_response.status_code == 200
        assert create_user4_response.json().get("username") == "Kuneringo12"
        assert create_user4_response.json().get("role") == "ROLE_USER"



    @pytest.mark.parametrize(
        "user1_login, user2_login, password_user1, password_user2, transfer",
        [
            ("Kuneringo9", "Kuneringo10", "Pas!sw0rd", "Pas!sw0rd", 499),
            ("Kuneringo11", "Kuneringo12", "Pas!sw0rd", "Pas!sw0rd", 10001)
        ]
    )
    def test_invalid_transfer(self, user1_login, user2_login, password_user1, password_user2, transfer):
        login_user_response = requests.post(
            url="http://localhost:4111/api/auth/token/login",
            json={
                "username": user1_login,
                "password": password_user1
            },
            headers={
                "Content-Type": "application/json",
                "accept": "application/json"
            }
        )

        assert login_user_response.status_code == 200
        token_user1 = login_user_response.json().get("token")

        create_account_user1_response = requests.post(
            url="http://localhost:4111/api/account/create",
            headers={
                "accept": "application/json",
                "Authorization": f"Bearer {token_user1}"
            }
        )


        assert create_account_user1_response.status_code == 201
        assert create_account_user1_response.json().get("balance") == 0
        account_user1_id = create_account_user1_response.json().get("id")

        deposit_user1_response = requests.post(
            url="http://localhost:4111/api/account/deposit",
            json={
                "accountId": account_user1_id,
                "amount": 1000
            },
            headers={
                "accept": "application/json",
                "Authorization": f"Bearer {token_user1}",
                "Content-Type": "application/json"
            }
        )

        assert deposit_user1_response.status_code == 200
        assert deposit_user1_response.json().get("balance") == 1000

        login_user2_response = requests.post(
            url="http://localhost:4111/api/auth/token/login",
            json={
                "username": user2_login,
                "password": password_user2
            },
            headers={
                "Content-Type": "application/json",
                "accept": "application/json"
            }
        )

        assert login_user2_response.status_code == 200
        token_user2 = login_user2_response.json().get("token")

        create_account_user2_response = requests.post(
            url="http://localhost:4111/api/account/create",
            headers={
                "accept": "application/json",
                "Authorization": f"Bearer {token_user2}"
            }
        )

        assert create_account_user2_response.status_code == 201
        assert create_account_user2_response.json().get("balance") == 0
        account_user2_id = create_account_user2_response.json().get("id")

        transfer_user2_response = requests.post(
            url="http://localhost:4111/api/account/transfer",
            json={
                "fromAccountId": account_user1_id,
                "toAccountId": account_user2_id,
                "amount": transfer
            },
            headers={
                "Content-Type": "application/json",
                "accept": "application/json",
                "Authorization": f"Bearer {token_user1}"
            }
        )

        assert transfer_user2_response.status_code == 400







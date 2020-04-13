import requests


def client():
    # credentials = {"username": "admin", "password": "admin"}

    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/",
    #                          data=credentials)

    token_h = "Token 1e0b7a0f13977b0038603d2e721578a742dc407c"
    headers = {"Authorization": token_h}

    response = requests.get("http://127.0.0.1:8000/api/profiles/",
                            headers=headers)

    print("Status Code: ", response.status_code)

    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()

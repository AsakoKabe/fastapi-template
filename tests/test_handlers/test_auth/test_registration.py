from starlette import status


class TestRegistration:
    @staticmethod
    def get_url() -> str:
        return "/api/v1/user/registration"

    async def test_base_scenario(self, client):
        data = {
            "username": "user",
            "password": "user-password",
            "email": "user@example.com"
        }
        response = await client.post(url=self.get_url(), json=data)
        assert response.status_code == status.HTTP_201_CREATED

    async def test_empty_username(self, client):
        data = {
            "username": "",
            "password": "user",
            "email": "user@example.com"
        }
        response = await client.post(url=self.get_url(), json=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    async def test_empty_password(self, client):
        data = {
            "username": "user",
            "password": "",
            "email": "user@example.com"
        }
        response = await client.post(url=self.get_url(), json=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    async def test_empty_email(self, client):
        data = {
            "username": "user",
            "password": "user",
            "email": ""
        }
        response = await client.post(url=self.get_url(), json=data)
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    async def test_empty_all(self, client):
        data = {
            "username": "",
            "password": "",
            "email": ""
        }
        response = await client.post(url=self.get_url(), json=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    async def test_same_username(self, client):
        data = {
            "username": "user",
            "password": "user-password",
            "email": "user@example.com"
        }
        response = await client.post(url=self.get_url(), json=data)
        assert response.status_code == status.HTTP_201_CREATED

        response = await client.post(url=self.get_url(), json=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

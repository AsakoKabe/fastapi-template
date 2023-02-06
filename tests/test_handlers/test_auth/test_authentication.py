from starlette import status


class TestAuthentication:
    @staticmethod
    def get_url() -> str:
        return "/api/v1/user/authentication"

    async def test_base_scenario(self, client, user_sample):
        data = {
            "username": "user",
            "password": "user-password",
        }
        response = await client.post(url=self.get_url(), data=data)
        assert response.status_code == status.HTTP_200_OK

    async def test_bad_password(self, client, user_sample):
        data = {
            "username": "user",
            "password": "user-user",
        }
        response = await client.post(url=self.get_url(), data=data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    async def test_not_exist_user(self, client, user_sample):
        data = {
            "username": "user123",
            "password": "user-user",
        }
        response = await client.post(url=self.get_url(), data=data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    async def test_empty_username(self, client, user_sample):
        data = {
            "username": "",
            "password": "user-user",
        }
        response = await client.post(url=self.get_url(), data=data)
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    async def test_empty_password(self, client, user_sample):
        data = {
            "username": "user",
            "password": "",
        }
        response = await client.post(url=self.get_url(), data=data)
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

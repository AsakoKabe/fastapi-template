from starlette import status


class TestMe:
    @staticmethod
    def get_url() -> str:
        return "/api/v1/user/me"

    @staticmethod
    def get_auth_url() -> str:
        return "/api/v1/user/authentication"

    async def test_base_scenario(self, client, user_sample):
        data = {
            "username": "user",
            "password": "user-password",
        }
        response = await client.post(url=self.get_auth_url(), data=data)
        assert response.status_code == status.HTTP_200_OK

        response = response.json()
        token = response['access_token']

        response = await client.get(
            url=self.get_url(),
            headers={"Authorization": f'Bearer {token}'}
        )
        assert response.status_code == status.HTTP_200_OK

    async def test_bad_token(self, client, user_sample):
        response = await client.get(
            url=self.get_url(),
            headers={"Authorization": 'Bearer dgsdg1312'}
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

from app.utils.user import get_user, register_user, delete_user
from app.schemas.auth.registration import RegistrationForm


class TestFunctionUserDatabase:
    async def test_get_user(
        self,
        client,
        user_sample,
        session
    ):
        user = await get_user(session, 'user')
        assert user == user_sample

        user = await get_user(session, 'not_exist')
        assert user is None

    async def test_register_user(
        self,
        client,
        user_sample,
        session
    ):
        new_user = RegistrationForm(
            username='user2',
            password='password2',
            email='user@example.com'
        )
        verdict, message = await register_user(session, new_user)
        assert verdict
        assert message == "Successful registration!"

        new_user = RegistrationForm(
            username='user',
            password='password2',
            email='user@example.com'
        )
        verdict, message = await register_user(session, new_user)
        assert not verdict
        assert message == "Username already exists."

    async def test_delete_user(
        self,
        client,
        user_sample,
        session
    ):
        await delete_user(session, user_sample)
        user = await get_user(session, 'user')
        assert user is None

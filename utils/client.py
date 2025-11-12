import aiohttp


class Client:
    @staticmethod
    async def auth(
        login: str,
        password: str
    ) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url="http://localhost:8000/auth/login",
                json=dict(login=login, password=password)
            ) as response:
                return await response.json()
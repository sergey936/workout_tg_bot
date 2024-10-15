from dataclasses import dataclass

from httpx import AsyncClient

from exceptions.user import (
    RegistrationRequestError,
    GetTokenRequestError,
    SetTelegramIDError,
)
from domain.services.user.base import BaseUserService


@dataclass
class UserWebService(BaseUserService):
    http_client: AsyncClient
    base_url: str
    api_token: str

    async def create_user(
        self,
        email: str,
        password: str,
        first_name: str,
        second_name: str,
        patronymic: str,
    ) -> None:
        create_user_response = await self.http_client.post(
            url=f"{self.base_url}users/",
            json={
                "name": first_name,
                "surname": second_name,
                "patronymic": patronymic,
                "email": email,
                "password": password,
            },
        )

        if not create_user_response.is_success:
            raise RegistrationRequestError(
                status_code=create_user_response.status_code,
                response_content=create_user_response.content.decode(),
            )

    async def get_token(
        self,
        email: str,
        password: str,
    ) -> str:
        get_token_response = await self.http_client.post(
            url=f"{self.base_url}auth/token",
            data={
                "username": email,
                "password": password,
            },
        )

        if not get_token_response.is_success:
            raise GetTokenRequestError(
                status_code=get_token_response.status_code,
                response_content=get_token_response.content.decode(),
            )

        return get_token_response.json()["access_token"]

    async def set_tg_id(
        self,
        token: str,
        tg_id: str,
    ) -> None:

        set_tg_id_response = await self.http_client.put(
            url=f"{self.base_url}users/set-telegram-id",
            headers={
                "Authorization": f"Bearer {token}",
                "api-token": self.api_token,
                "tg-user-id": str(tg_id),
            },
        )

        if not set_tg_id_response.is_success:
            raise SetTelegramIDError(
                status_code=set_tg_id_response.status_code,
                response_content=set_tg_id_response.content.decode(),
            )

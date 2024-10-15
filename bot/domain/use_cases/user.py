from dataclasses import dataclass

from domain.dtos.user import UserDTO
from domain.services.user.base import BaseUserService
from domain.use_cases.base import BaseUseCase


@dataclass
class RegistrationUserCommand:
    user: UserDTO


@dataclass
class RegistrationUseCase(BaseUseCase[RegistrationUserCommand, None]):
    user_service: BaseUserService

    async def execute(self, command: RegistrationUserCommand) -> None:
        await self.user_service.create_user(
            email=command.user.email,
            password=command.user.password,
            first_name=command.user.first_name,
            second_name=command.user.second_name,
            patronymic=command.user.patronymic,
        )

        token = await self.user_service.get_token(
            email=command.user.email,
            password=command.user.password,
        )

        await self.user_service.set_tg_id(
            token=token,
            tg_id=command.user.tg_id,
        )

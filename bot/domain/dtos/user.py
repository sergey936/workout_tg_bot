from dataclasses import dataclass


@dataclass
class UserDTO:
    tg_id: str

    email: str
    password: str

    first_name: str
    second_name: str
    patronymic: str = 'TELEGRAM'

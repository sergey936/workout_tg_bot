from pydantic_settings import BaseSettings
from pydantic import Field


class Config(BaseSettings):
    bot_token: str = Field(
        default="7186170740:AAHEYHJLdIHLW0Qr9JdlZRUuTVM4SxwixmU",
        alias="TG_BOT_TOKEN",
    )
    base_url: str = Field(
        alias="WEB_API_BASE_URL", default="http://localhost:8000/"
    )

    api_token: str = Field(
        default="a1b2c3d4e5f67890abcdefabcdef234567890abcdefabcdefabcdefabcdef1234",
        alias="API_TOKEN",
    )

import json
from dataclasses import dataclass


@dataclass(frozen=True, eq=False)
class ApplicationException(Exception):
    @property
    def message(self):
        return "Application Error"


@dataclass(frozen=True, eq=False)
class BaseWebException(ApplicationException):
    status_code: int
    response_content: str

    @property
    def response_json(self) -> dict:
        return json.loads(self.response_content)

    @property
    def error_text(self) -> dict:
        return self.response_json.get("detail", {}).get("error", "")

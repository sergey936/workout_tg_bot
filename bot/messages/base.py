from typing import Any


class BaseMessageBuilder:
    _text: str = ""
    _reply_markup: Any = None

    def build(self) -> Any | None:
        message = {"text": self._text}

        if self._reply_markup:
            message["reply_markup"] = self._reply_markup

        return message

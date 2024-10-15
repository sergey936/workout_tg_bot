from dataclasses import dataclass

from exceptions.base import BaseWebException


@dataclass(frozen=True, eq=False)
class CreateWorkoutRequestError(BaseWebException):

    @property
    def message(self):
        return 'Create workout error'

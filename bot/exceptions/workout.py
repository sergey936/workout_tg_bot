from dataclasses import dataclass

from exceptions.base import BaseWebException


@dataclass(frozen=True, eq=False)
class CreateWorkoutRequestError(BaseWebException):

    @property
    def message(self):
        return 'Create workout error'


@dataclass(frozen=True, eq=False)
class GetAllWorkoutsRequestError(BaseWebException):

    @property
    def message(self):
        return 'Get workouts error'


@dataclass(frozen=True, eq=False)
class UploadWorkoutFileRequestError(BaseWebException):

    @property
    def message(self):
        return 'Upload workout error'

from collections.abc import Iterable
from dataclasses import dataclass
from io import BytesIO

from domain.dtos.workout import WorkoutDTO
from domain.services.workout.base import BaseWorkoutService
from domain.use_cases.base import BaseUseCase, C, R


@dataclass
class GetAllWorkoutsCommand:
    limit: int
    offset: int
    tg_id: int



@dataclass
class GetAllWorkoutsUseCase(BaseUseCase[GetAllWorkoutsCommand, Iterable[WorkoutDTO] | None]):
    workout_service: BaseWorkoutService

    async def execute(self, command: GetAllWorkoutsCommand) -> Iterable[WorkoutDTO] | None:
        workouts = await self.workout_service.get_all_workouts(
            limit=command.limit,
            offset=command.offset,
            tg_id=command.tg_id,
        )

        return workouts


@dataclass
class CreateWorkoutCommand:
    title: str
    description: str
    tg_id: int
    file_format: str
    file: BytesIO | None = None
    


@dataclass
class CreateWorkoutUseCase(BaseUseCase[CreateWorkoutCommand, None]):
    workout_service: BaseWorkoutService

    async def execute(self, command: CreateWorkoutCommand) -> None:
        workout = await self.workout_service.create_workout(
            title=command.title,
            description=command.description,
            tg_id=command.tg_id,
        )

        await self.workout_service.upload_workout_file(
            file=command.file,
            workout_id=workout['id'],
            tg_id=command.tg_id,
            file_format=command.file_format,
        )

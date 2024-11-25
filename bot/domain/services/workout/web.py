from dataclasses import dataclass
from io import BytesIO
from typing import Iterable, Any

from domain.dtos.workout import WorkoutDTO
from domain.services.workout.base import BaseWorkoutService

from exceptions.workout import CreateWorkoutRequestError, GetAllWorkoutsRequestError, UploadWorkoutFileRequestError

from httpx import AsyncClient


@dataclass
class WebWorkoutService(BaseWorkoutService):
    http_client: AsyncClient
    base_url: str
    api_token: str

    async def create_workout(self, title: str, description: str, tg_id: int) -> dict[str, Any]:
        response = await self.http_client.post(
            url=f'{self.base_url}workouts/',
            json={
                'title': title,
                'description': description,
            },
            headers={
                'api-token': self.api_token,
                'tg-user-id': str(tg_id),
                'Authorization': 'Bearer',
            },
        )

        if not response.is_success:
            raise CreateWorkoutRequestError(
                status_code=response.status_code,
                response_content=response.content.decode(),
            )

        return response.json()

    async def upload_workout_file(self, file: BytesIO, workout_id: str, tg_id: int, file_format: str) -> None:
        response = await self.http_client.put(
            url=f'{self.base_url}workouts/add-file',
            params={
                'workout_id': workout_id,
            },
            files={
                'file': (f'filename.{file_format}', file),
            },
            headers={
                'api-token': self.api_token,
                'tg-user-id': str(tg_id),
                'Authorization': 'Bearer',
            },
        )

        if not response.is_success:
            raise UploadWorkoutFileRequestError(
                status_code=response.status_code,
                response_content=response.content.decode(),
            )

    async def get_all_workouts(self, limit: int, offset: int, tg_id: int) -> Iterable[WorkoutDTO] | None:
        response = await self.http_client.get(
            url=f'{self.base_url}workouts/',
            params={
                'limit': limit,
                'offset': offset,
                'order': False,
            },
            headers={
                'api-token': self.api_token,
                'tg-user-id': str(tg_id),
                'Authorization': 'Bearer',
            },
        )
        if not response.is_success:
            raise GetAllWorkoutsRequestError(
                status_code=response.status_code,
                response_content=response.content.decode(),
            )

        return [WorkoutDTO.from_web(workout=workout) for workout in response.json()['items']]
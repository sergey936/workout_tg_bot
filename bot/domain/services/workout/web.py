from dataclasses import dataclass

from domain.services.workout.base import BaseWorkoutService

from exceptions.workout import CreateWorkoutRequestError

from httpx import AsyncClient


@dataclass
class WebWorkoutService(BaseWorkoutService):
    http_client: AsyncClient
    base_url: str
    api_token: str

    async def create_workout(self, title: str, description: str) -> None:
        response = await self.http_client.post(
            url=f'{self.base_url}/Workouts/',
            json={
                'title': title,
                'description': description,
            },
        )

        if not response.is_success:
            raise CreateWorkoutRequestError(
                status_code=response.status_code,
                response_content=response.content.decode(),
            )

    async def upload_workout_file(self):
        ...

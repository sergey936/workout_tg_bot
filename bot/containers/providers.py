from aiogram import Bot, Dispatcher

from dishka import Provider, Scope, provide

from domain.services.user.web import UserWebService
from domain.services.workout.web import WebWorkoutService
from domain.use_cases.user import CheckTGUserExistsUseCase, RegistrationUseCase

from httpx import AsyncClient

from domain.use_cases.workouts import GetAllWorkoutsUseCase, CreateWorkoutUseCase, GetWorkoutUseCase
from settings.config import Config


class DefaultProvider(Provider):
    @provide(scope=Scope.APP)
    def get_settings(self) -> Config:
        return Config()

    @provide(scope=Scope.APP)
    def get_telegram_bot(self) -> tuple[Bot, Dispatcher]:
        return Bot(token=self.get_settings().bot_token), Dispatcher()

    @provide(scope=Scope.REQUEST)
    def get_http_client(self) -> AsyncClient:
        return AsyncClient()

    @provide(scope=Scope.REQUEST)
    def get_user_web_service(self) -> UserWebService:
        return UserWebService(
            http_client=self.get_http_client(),
            base_url=self.get_settings().base_url,
            api_token=self.get_settings().api_token,
        )

    @provide(scope=Scope.REQUEST)
    def get_workout_web_service(self) -> WebWorkoutService:
        return WebWorkoutService(
            http_client=self.get_http_client(),
            base_url=self.get_settings().base_url,
            api_token=self.get_settings().api_token,
        )

    @provide(scope=Scope.REQUEST)
    def get_registration_use_case(self) -> RegistrationUseCase:
        return RegistrationUseCase(
            user_service=self.get_user_web_service(),
        )

    @provide(scope=Scope.REQUEST)
    def get_check_user_exists_use_case(self) -> CheckTGUserExistsUseCase:
        return CheckTGUserExistsUseCase(
            user_service=self.get_user_web_service(),
        )

    @provide(scope=Scope.REQUEST)
    def get_all_workouts_use_case(self) -> GetAllWorkoutsUseCase:
        return GetAllWorkoutsUseCase(
            workout_service=self.get_workout_web_service(),
        )

    @provide(scope=Scope.REQUEST)
    def get_create_workout_use_case(self) -> CreateWorkoutUseCase:
        return CreateWorkoutUseCase(
            workout_service=self.get_workout_web_service()
        )

    @provide(scope=Scope.REQUEST)
    def get_workout_info_use_case(self) -> GetWorkoutUseCase:
        return GetWorkoutUseCase(
            workout_service=self.get_workout_web_service()
        )

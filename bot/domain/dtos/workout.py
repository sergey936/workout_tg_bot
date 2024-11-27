from dataclasses import dataclass

from callbacks.workout import WorkoutCbData


@dataclass
class WorkoutDTO:
    id: str
    trainer_id: str
    title: str
    description: str
    file_path: str

    @classmethod
    def from_web(cls, workout: dict) -> 'WorkoutDTO':
        return cls(
            id=workout['id'],
            trainer_id=workout['trainer_id'],
            title=workout['title'],
            description=workout['description'],
            file_path=workout['file_path'],
        )

from abc import ABC, abstractmethod


class BaseUseCase(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def execute(self):
        pass

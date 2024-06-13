from abc import abstractmethod, ABC
from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Shape(ABC):

    name: str | None = field(default=None, compare=False)

    @abstractmethod
    def translate(self, delta_x: float, delta_y: float) -> None:
        pass

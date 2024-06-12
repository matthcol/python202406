from dataclasses import dataclass


@dataclass
class City:
    # attributes
    name: str
    population: int
    code_postal: str

    # methods
    def copy(self):
        return City(name=self.name, population=self.population, code_postal=self.code_postal)
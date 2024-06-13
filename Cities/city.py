from dataclasses import dataclass

# decorator @dataclass generates:
#   __init__ (constructor): City(...)
#   __repr__ (and __str__ by default): builtins str(), repr(), print, f-string
#   __eq__ (equals)  __ne__ (not equals): operators == and !=
# (opt)  __lt__ (less than) + __le__ + __gt__ + __ge__: operators < <= > >=
@dataclass(order=True)
class City:
    # attributes
    name: str
    population: int
    code_postal: str

    # methods

    def __str__(self):
        return f"{self.name} ({self.code_postal}, {self.population} hab)"


    def copy(self):
        return City(name=self.name, population=self.population, code_postal=self.code_postal)
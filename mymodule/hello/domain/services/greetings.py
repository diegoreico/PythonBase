
from mymodule.hello.domain.entities.person import Person


class GreetingsService:

    def say_hello_to(self, person: Person) -> str:
        return f"Hello {person.name}!"
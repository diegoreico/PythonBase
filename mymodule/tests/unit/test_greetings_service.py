from mymodule.hello.domain.entities.person import Person
from mymodule.hello.domain.services.greetings import GreetingsService

def test_greetings_service_greets_person_appending_name():
    name = "Patatas"
    person = Person(name=name)
    service = GreetingsService()
    
    expected = f"Hello {name}!"
    result = service.say_hello_to(person)

    assert expected == result

from data.data import Person
from faker import Faker

faker = Faker('en_US')
Faker.seed()

def generated_person():
    yield Person(
        full_name=faker.name(),
        email=faker.ascii_free_email(),
        current_address=faker.address(),
        permanent_address=faker.address(),
    )
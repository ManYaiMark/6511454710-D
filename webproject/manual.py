from faker import Faker
from search.models import *

fake = Faker()

for _ in range(10):
  Course.objects.create(
    Course_id = fake.unique.bothify(text='#####'),
    Course_name = fake.catch_phrase(),
    Teacher_name = fake.name()
  )
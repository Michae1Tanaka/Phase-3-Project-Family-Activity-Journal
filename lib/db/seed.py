from faker import Faker
import random
from random import choice as rc

fake = Faker()

choices = ["1", "3", "5"]
chosen = rc(choices)
print(chosen)

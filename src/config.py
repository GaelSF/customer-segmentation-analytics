from faker import Faker
import random
import numpy as np

RANDOM_SEED = 42
N_CUSTOMERS = 10_000

random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)

fake = Faker("es_MX")
Faker.seed(RANDOM_SEED)

MEMBERSHIPS = [
    "Basic",
    "Gold",
    "Platinum"
]

MEMBERSHIP_PROBABILITIES = [
    0.70,
    0.25,
    0.05
]
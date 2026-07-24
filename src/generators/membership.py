import numpy as np

from config import (
    MEMBERSHIPS,
    MEMBERSHIP_PROBABILITIES
)


def generate_membership():

    return np.random.choice(
        MEMBERSHIPS,
        p=MEMBERSHIP_PROBABILITIES
    )
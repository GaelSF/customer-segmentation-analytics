"""
Demographic data generators.

Generates synthetic demographic information
for customers.
"""


import numpy as np


# =============================================================================
# Constants
# =============================================================================


GENDERS = [
    "Female",
    "Male"
]


MEXICAN_LOCATIONS = {

    "Ciudad de México": {
        "weight": 0.30,
        "cities": [
            "Coyoacán",
            "Benito Juárez",
            "Miguel Hidalgo",
            "Álvaro Obregón"
        ]
    },

    "Estado de México": {
        "weight": 0.30,
        "cities": [
            "Naucalpan",
            "Tlalnepantla",
            "Ecatepec",
            "Toluca"
        ]
    },

    "Jalisco": {
        "weight": 0.22,
        "cities": [
            "Guadalajara",
            "Zapopan",
            "Tlaquepaque"
        ]
    },

    "Nuevo León": {
        "weight": 0.18,
        "cities": [
            "Monterrey",
            "San Nicolás",
            "Guadalupe"
        ]
    }

}


# =============================================================================
# Generators
# =============================================================================


def generate_gender() -> str:
    """
    Generate customer gender.
    """

    return np.random.choice(
        GENDERS
    )



def generate_age() -> int:
    """
    Generate customer age.

    Assumes an adult customer population.
    """

    age = np.random.normal(
        loc=38,
        scale=12
    )

    return int(
        np.clip(
            age,
            18,
            80
        )
    )



def generate_state() -> str:
    """
    Generate Mexican state according
    to predefined population weights.
    """

    states = list(
        MEXICAN_LOCATIONS.keys()
    )

    weights = [
        MEXICAN_LOCATIONS[state]["weight"]
        for state in states
    ]

    return np.random.choice(
        states,
        p=weights
    )



def generate_city(state: str) -> str:
    """
    Generate city according to state.
    """

    cities = MEXICAN_LOCATIONS[state]["cities"]

    return np.random.choice(
        cities
    )
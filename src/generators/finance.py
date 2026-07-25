"""
Financial customer generators.
"""


import numpy as np



def generate_income(membership: str) -> int:
    """
    Generate annual income in MXN.
    """

    if membership == "Basic":

        return np.random.randint(
            120_000,
            350_000
        )

    elif membership == "Gold":

        return np.random.randint(
            350_000,
            700_000
        )

    else:

        return np.random.randint(
            700_000,
            1_500_000
        )



def generate_credit_limit(
    membership: str,
    annual_income: int
) -> float:
    """
    Generate credit limit based on income.
    """

    factors = {

        "Basic": 0.20,

        "Gold": 0.35,

        "Platinum": 0.50

    }

    return round(
        annual_income * factors[membership],
        2
    )



def generate_transactions(
    membership: str
) -> int:
    """
    Generate monthly transactions.
    """

    if membership == "Basic":

        return np.random.poisson(8)

    elif membership == "Gold":

        return np.random.poisson(18)

    else:

        return np.random.poisson(35)



def generate_average_ticket(
    membership: str
) -> float:
    """
    Generate average purchase amount.
    """

    if membership == "Basic":

        return np.random.normal(
            500,
            150
        )

    elif membership == "Gold":

        return np.random.normal(
            900,
            250
        )

    else:

        return np.random.normal(
            1800,
            500
        )



def generate_total_spending(
    transactions: int,
    average_ticket: float
) -> float:
    """
    Estimate monthly spending.
    """

    return round(
        transactions * average_ticket,
        2
    )
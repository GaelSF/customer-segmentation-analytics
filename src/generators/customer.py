import pandas as pd
from generators.membership import generate_membership
from generators.demographics import (
    generate_gender,
    generate_age,
    generate_state,
    generate_city
)
from generators.finance import (
    generate_income,
    generate_credit_limit,
    generate_transactions,
    generate_average_ticket,
    generate_total_spending
)




def generate_customer(customer_id: int) -> dict:
    """
    Generate one synthetic customer.
    """

    membership = generate_membership()

    annual_income = generate_income(
    membership
    )

    transactions = generate_transactions(
    membership
    )

    average_ticket = generate_average_ticket(
    membership
    )

    state = generate_state()

    customer = {

        "customer_id": customer_id,

        "membership": membership,

        "gender": generate_gender(),

        "age": generate_age(),

        "state": state,

        "city": generate_city(state),

        "annual_income": annual_income,

        "credit_limit": generate_credit_limit(
            membership,
            annual_income
        ),

        "monthly_transactions": transactions,

        "average_ticket": round(
            average_ticket,
            2
        ),

        "monthly_spending": generate_total_spending(
            transactions,
            average_ticket
        )

    }

    return customer

def generate_dataset(n_customers: int) -> pd.DataFrame:

    customers = []

    for customer_id in range(1, n_customers + 1):

        customers.append(
            generate_customer(customer_id)
        )

    return pd.DataFrame(customers)
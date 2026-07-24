import pandas as pd

from generators.membership import generate_membership


def generate_customer(customer_id: int) -> dict:

    return {
        "customer_id": customer_id,
        "membership": generate_membership()
    }


def generate_dataset(n_customers: int) -> pd.DataFrame:

    customers = []

    for customer_id in range(1, n_customers + 1):

        customers.append(
            generate_customer(customer_id)
        )

    return pd.DataFrame(customers)
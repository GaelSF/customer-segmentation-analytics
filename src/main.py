from config import N_CUSTOMERS
from generators.customer import generate_dataset


def main():

    df = generate_dataset(N_CUSTOMERS)

    print(df.head())

    print()

    print(df.info())


if __name__ == "__main__":
    main()
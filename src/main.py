#from generators.membership import generate_membership
from config import N_CUSTOMERS
from generators.customer import generate_dataset

def main():

    #print("\nMembership Generator\n")

    #for _ in range(10):

    #    print(generate_membership())

    df = generate_dataset(N_CUSTOMERS)

    print(df.head())

    print()

    print(df["membership"].value_counts())



if __name__ == "__main__":
    main()
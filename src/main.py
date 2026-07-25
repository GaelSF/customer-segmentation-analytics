from config import N_CUSTOMERS
from generators.customer import generate_dataset


def main():

    df = generate_dataset(N_CUSTOMERS)

    print(df.head())

    print()

    print(df.info())

    print('=' * 30)
    print("Description of customer dataset\n")
    print('=' * 30)

    msp = df.sort_values("monthly_spending", ascending=False).head(10)
    m_m_ave = df.groupby("membership")["monthly_spending"].mean()
    m_s_ave = df.groupby("state")["monthly_spending"].mean()

    print("Top 10 customers by monthly spending:\n")
    print(msp)

    print("\nAverage monthly spending by membership:\n")
    print(m_m_ave)

    print("\nAverage monthly spending by state:\n")
    print(m_s_ave)
    

if __name__ == "__main__":
    main()
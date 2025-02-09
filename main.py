import pandas as pd

# Load data
cards_df = pd.read_csv("D:\\University\\BI\\cards_data.csv")
transactions_df = pd.read_csv("D:\\University\\BI\\transactions_data.csv")
users_df = pd.read_csv("D:\\University\\BI\\users_data.csv")

# Merge transactions with users and cards
fact_transactions = transactions_df.merge(users_df, left_on="client_id", right_on="id", suffixes=("", "_user"))
fact_transactions = fact_transactions.merge(cards_df, left_on="card_id", right_on="id", suffixes=("", "_card"))

# Drop redundant columns
fact_transactions.drop(columns=["id_user", "id_card"], inplace=True)


# Convert currency columns to float
def convert_currency(column):
    return column.replace({'\$': '', ',': ''}, regex=True).astype(float)


fact_transactions["amount"] = convert_currency(fact_transactions["amount"])
fact_transactions["yearly_income"] = convert_currency(fact_transactions["yearly_income"])
fact_transactions["total_debt"] = convert_currency(fact_transactions["total_debt"])
fact_transactions["credit_limit"] = convert_currency(fact_transactions["credit_limit"])

# Prepare dimension tables
dim_client = users_df.rename(columns={"id": "client_id"})[
    [
        "client_id",
        "gender",
        "current_age",
        "address",
        "per_capita_income"
    ]
]
dim_client["per_capita_income"] = convert_currency(dim_client["per_capita_income"])

dim_card = cards_df.rename(columns={"id": "card_id"})[
    [
        "card_id",
        "card_brand",
        "card_type",
        "credit_limit",
        "has_chip"
    ]
]
dim_card["credit_limit"] = convert_currency(dim_card["credit_limit"])

# Convert date column to datetime format
fact_transactions["date"] = pd.to_datetime(fact_transactions["date"])

# Create date dimension table
dim_date = pd.DataFrame({
    "date_id": fact_transactions["date"].dt.strftime("%Y-%m-%d"),
    "year": fact_transactions["date"].dt.year,
    "month": fact_transactions["date"].dt.month,
    "day": fact_transactions["date"].dt.day,
})

# Save to Excel
with pd.ExcelWriter("Financial_Transactions.xlsx") as writer:
    fact_transactions.to_excel(writer, sheet_name="fact_transactions", index=False)
    dim_client.to_excel(writer, sheet_name="dim_client", index=False)
    dim_card.to_excel(writer, sheet_name="dim_card", index=False)
    dim_date.to_excel(writer, sheet_name="dim_date", index=False)

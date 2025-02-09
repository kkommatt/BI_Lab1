# Financial Transactions Data Analysis

This repository contains a comprehensive analysis of credit card transaction data, focusing on various aspects of consumer behavior, transaction patterns, and credit-related factors. The data includes transaction details, user profiles, and card information, which are processed and analyzed using Python and Excel.

## Data Sources
- **cards_data.csv**: Information about the credit cards, including card type, brand, credit limit, and chip availability.
- **transactions_data.csv**: Transaction details, including transaction amount, date, merchant information, and transaction method.
- **users_data.csv**: User profiles, including demographics like age, income, credit score, and number of credit cards.

## Data Preparation
1. The data from the three CSV files is merged into a consolidated dataset for analysis.
2. Relevant dimensions (clients, cards, and dates) are extracted and processed.
3. Currency values are cleaned and converted to a numerical format for accurate analysis.
4. A consolidated Excel file (`Financial_Transactions.xlsx`) is created, containing the fact table and dimension tables.

## Analysis
The following key analyses were performed:
- **Time-Based Analysis**: Total transaction amounts over time, filtered by card brand (Mastercard/Visa).
- **Customer Spending Behavior**: Spending behavior of customers segmented by card brand and gender.
- **Credit Score Impact**: How credit scores impact transaction amounts and total debt, with filters based on the number of credit cards.

## Tools
- Python (pandas) for data processing and merging.
- Excel Pivot Tables for data visualization and analysis.

## Getting Started
1. Clone this repository.
2. Run the provided Python scripts to prepare and clean the data.
3. Open the `Financial_Transactions.xlsx` file to explore the analysis and visualizations in Excel.


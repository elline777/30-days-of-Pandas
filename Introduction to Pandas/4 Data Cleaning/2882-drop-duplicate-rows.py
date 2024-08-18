import pandas as pd


def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers.drop_cuplicates(subset=['email'], keep='first', inplace=True)
    return customers
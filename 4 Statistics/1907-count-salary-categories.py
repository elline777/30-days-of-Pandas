import pandas as pd

data = [[3, 108939], [2, 12747], [8, 87709], [6, 91796]]
accounts = pd.DataFrame(data, columns=['account_id', 'income']).astype(
    {'account_id': 'Int64', 'income': 'Int64'})


def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low = accounts[accounts.income < 20000].income.count()
    average = accounts[accounts.income.between(20000, 50000)].income.count()
    high = accounts[accounts.income > 50000].income.count()

    result = pd.DataFrame(data=[
        ['Low Salary', low],
        ['Average Salary', average],
        ['High Salary', high]
    ],
        columns=['category', 'accounts_count'])
    return result

print(count_salary_categories(accounts))

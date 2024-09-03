import pandas as pd

data = [[1, 100], [2, 200], [3, 300], [4, 300]]
employee = pd.DataFrame(data, columns=['Id', 'salary']).astype(
    {'Id': 'Int64', 'salary': 'Int64'})


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee.drop_duplicates(subset=['salary'], inplace=True)
    if N > len(employee) or N < 1:
        result = None
    else:
        result = employee.sort_values(by='salary', ascending=False) \
            .reset_index(drop=True) \
            .iloc[N - 1, 1]
    return pd.DataFrame({f'getNthHighestSalary({N})': [result]})


print(nth_highest_salary(employee, 40))

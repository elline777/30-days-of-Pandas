import pandas as pd

data = [[1, 100], [2, 200], [3, 300], [4, 200]]
employee = pd.DataFrame(data, columns=['id', 'salary']).astype(
    {'id': 'int64', 'salary': 'int64'})


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    if employee.salary.nunique() < 2:
        result = None
    else:
        result = employee.salary.drop_duplicates().nlargest(2).iloc[-1]
    return pd.DataFrame({'SecondHighestSalary': [result]})


print(second_highest_salary(employee))

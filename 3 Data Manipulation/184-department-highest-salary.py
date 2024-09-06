import pandas as pd

data = [[1, 'Joe', 70000, 1], [2, 'Jim', 90000, 1], [3, 'Henry', 80000, 2],
        [4, 'Sam', 60000, 2], [5, 'Max', 90000, 1]]
employee = pd.DataFrame(data, columns=['id', 'name', 'salary',
                                       'departmentId']).astype(
    {'id': 'Int64', 'name': 'object', 'salary': 'Int64',
     'departmentId': 'Int64'})
data = [[1, 'IT'], [2, 'Sales']]
department = pd.DataFrame(data, columns=['id', 'name']).astype(
    {'id': 'Int64', 'name': 'object'})


def department_highest_salary(employee: pd.DataFrame,
                              department: pd.DataFrame) -> pd.DataFrame:
    merged_df = employee.merge(department, left_on='departmentId', right_on='id')
    merged_df = merged_df.rename(columns={'name_x': 'Employee', 'salary': 'Salary', 'name_y': 'Department'})[['Department', 'Employee', 'Salary']]
    return merged_df[merged_df['Salary'] == merged_df.groupby('Department')['Salary'].transform('max')]


print(department_highest_salary(employee, department))

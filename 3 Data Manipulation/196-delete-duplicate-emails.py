import pandas as pd

data = [[1, 'john@example.com'], [2, 'bob@example.com'],
        [3, 'john@example.com']]
person = pd.DataFrame(data, columns=['id', 'email']).astype(
    {'id': 'int64', 'email': 'object'})


def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values('id', inplace=True)
    person.drop_duplicates(subset=['email'], inplace=True)


delete_duplicate_emails(person)
print(person)

import pandas as pd

def selectData(students: pd.DataFrame) ->pd.DataFrame:
    return students.loc[students[id] == 101, ['name', 'age']]
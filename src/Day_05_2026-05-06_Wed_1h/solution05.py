# LC 2880 — Select Data
import pandas as pd
def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students['student_id'] == 101, ['name', 'age']]

# LC 2881 — Create a New Column
def createNewColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees["salary"] * 2
    return employees

# LC 2882 — Drop Duplicate Rows
def dropDuplicateRows(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates(subset=["email"], keep="first")




if __name__ == "__main__":
    import os
    students = pd.read_csv(os.path.join(os.path.dirname(__file__), "01_LC_2880_select_data/data/students.csv"))
    print(selectData(students))
    employees = pd.read_csv(os.path.join(os.path.dirname(__file__), "02_LC_2881_create_new_column/data/employees.csv"))
    print(createNewColumn(employees))
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), "03_LC_2882_drop_duplicates/data/customers.csv"))
    print(dropDuplicateRows(df))  

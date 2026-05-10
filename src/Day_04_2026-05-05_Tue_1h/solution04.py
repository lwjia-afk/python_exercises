# LC 2877 — Create a DataFrame from List
import pandas as pd
def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns = ["student_id","age"])

def createDataframeWithRecode(student_data: list[list[int]]) -> pd.DataFrame:
    return pd.DataFrame.from_records(student_data, columns = ["student_id","age"])

# LC 2878 — Get the Size of a DataFrame
def getDataframeSize(df: pd.DataFrame) -> list[int]:
    return list(df.shape)
# LC 2879 — Display the First Three Rows
def displayFirstThreeRows(df: pd.DataFrame) -> pd.DataFrame:
    return df.head(3)


if __name__ == "__main__":
    student_data = [[1, 20], [2, 21], [3, 22]]
    print(createDataframe(student_data))
    print(createDataframeWithRecode(student_data)) 
    import os
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), "02_LC_2878_dataframe_size/data/players.csv"))
    print(getDataframeSize(df))      
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), "03_LC_2879_first_three_rows/data/employees.csv"))
    print(displayFirstThreeRows(df))                 
                                            
# LC 2891 — Method Chaining
import pandas as pd

def methodChaining(df: pd.DataFrame) -> pd.DataFrame:
    return df.loc[df["weight"] > 100].sort_values("weight", ascending=False)[["name"]]





if __name__ == "__main__":
    import os
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), "01_LC_2891_method_chaining/data/animals.csv"))
    print(methodChaining(df))

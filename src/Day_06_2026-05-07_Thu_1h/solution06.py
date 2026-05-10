# LC 2883 — Drop Missing Data
import pandas as pd
def dropMissingData(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna(subset = ["name"], how = "any")

# LC 2887 — Fill Missing Data
def fillMissingData(df: pd.DataFrame) -> pd.DataFrame:
    df.loc[df["quantity"].isna(), "quantity"] = 0
    return df

# LC 2888 — Reshape Data: Concatenate
def reshapeData(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1,df2], axis=0, ignore_index=True)


if __name__ == "__main__":
    import os
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), "01_LC_2883_drop_missing/data/students.csv"))
    print(dropMissingData(df))
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), "02_LC_2887_fill_missing/data/products.csv"))
    print(fillMissingData(df))
    df1 = pd.read_csv(os.path.join(os.path.dirname(__file__), "03_LC_2888_concatenate/data/df1.csv"))
    df2 = pd.read_csv(os.path.join(os.path.dirname(__file__), "03_LC_2888_concatenate/data/df2.csv"))
    print(reshapeData(df1, df2))

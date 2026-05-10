# Pandas groupby + aggregation
import pandas as pd

def quantitybyregion(df: pd.DataFrame) -> pd.DataFrame:
    print("quantity by region")
    return df.groupby("region").agg({"quantity": "sum"})

def averagePriceByRegion(df: pd.DataFrame) -> pd.DataFrame:
    print("average price by region")
    return df.groupby("region").agg({"price": "mean"})

def totalRevenueByRegion(df: pd.DataFrame) -> pd.DataFrame:
    print("total revenue by region")
    df["revenue"]=df["quantity"] * df["price"]
    return df.groupby("region").agg({"revenue": "sum"})

def totalQuantityByRegionProduct(df: pd.DataFrame) -> pd.DataFrame:
    print("total quantity by region and product")
    return df.groupby(["region","product"]).agg({"quantity": "sum"})

def topRevenueByProduct(df: pd.DataFrame) -> pd.DataFrame:
    print("top revenue by product")
    df["revenue"]=df["quantity"] * df["price"]
    return df.groupby("product")["revenue"].sum().nlargest(2).reset_index()[["product"]]


if __name__ == "__main__":
    import os
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), "data/sales.csv"))

    print(quantitybyregion(df))
    print(averagePriceByRegion(df))
    print(totalRevenueByRegion(df))
    print(totalQuantityByRegionProduct(df))
    print(topRevenueByProduct(df))

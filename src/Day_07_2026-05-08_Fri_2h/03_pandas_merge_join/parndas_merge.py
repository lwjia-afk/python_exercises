# Pandas merge / join
import pandas as pd

def innerJoin(orders: pd.DataFrame, customers: pd.DataFrame) -> pd.DataFrame:
    print("innerJoin: customer_id is the common column in both dataframes")
    return pd.merge(orders, customers, how="inner", on="customer_id")


def leftJoin(orders: pd.DataFrame, customers: pd.DataFrame) -> pd.DataFrame:
    print("leftJoin: customer_id is the common column in both dataframes")
    return pd.merge(orders, customers, how="left", on="customer_id")


def customerWithoutOrders(orders: pd.DataFrame, customers: pd.DataFrame) -> pd.DataFrame:
    print("customerWithoutOrders: customer_id is the common column in both dataframes")
    return pd.merge(customers, orders, how="left", on="customer_id", indicator=True).loc[lambda x: x["_merge"] == "left_only"].drop(columns=["_merge"])








if __name__ == "__main__":
    import os
    customers = pd.read_csv(os.path.join(os.path.dirname(__file__), "data/customers.csv"))
    orders = pd.read_csv(os.path.join(os.path.dirname(__file__), "data/orders.csv"))
    print(innerJoin(customers=customers, orders=orders))
    print(leftJoin(customers=customers, orders=orders))
    print(customerWithoutOrders(orders=orders, customers=customers))


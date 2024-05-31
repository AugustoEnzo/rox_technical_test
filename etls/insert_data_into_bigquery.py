import pandas as pd
import pandas_gbq

### Extract
# import sales data to a pandas dataframe
sales_df = pd.read_excel("datasets/sales_data.csv.xlsx")

# import consumer data to a pandas dataframe
customer_df = pd.read_excel("datasets/customer_data.xlsx")

### Tranform
# renaming attribute for sales df
sales_df["client_id"] = sales_df["cliente_id"]

# dropping wrong named attribute for sales_df
sales_df = sales_df.drop(columns=["cliente_id"])

# renaming attribute for customer df
customer_df["client_id"] = customer_df["id_cliente"]

# dropping wrong name attribute for customer_df
customer_df = customer_df.drop(columns=["id_cliente"])

# creating final dataframe
# using pandas join operation
final_df = pd.merge(sales_df, customer_df, on="client_id", how="inner")
final_df["sales_value"] = final_df.quantity * final_df.unit_price

# selecting specific fields
final_df = final_df[["product_name", "quantity", "unit_price", "sales_value", "order_date", "email"]]
final_df["client_email"] = final_df["email"]

# drop wrong named column
final_df = final_df.drop(columns=["email"])

### Load
pandas_gbq.to_gbq(final_df, destination_table="rox_partner.sales", project_id="hazel-thunder-425017-p5", if_exists='replace')

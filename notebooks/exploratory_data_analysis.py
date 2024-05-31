import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import sales data to a pandas dataframe
sales_df = pd.read_excel("datasets/sales_data.csv.xlsx")

# renaming attribute for sales df
sales_df["client_id"] = sales_df["cliente_id"]

# dropping wrong named attribute
sales_df = sales_df.drop(columns=["cliente_id"])

# sales df exploratory data analysis
print("Distribution of null values between the attributes for sales df:")
print(sales_df.isnull().sum())
print("\n")

"""
With the distribution of null values we could notice that there are none null values in the sales dataframe
"""

print("Distribution of unique values between attributes of sales df:")
print(sales_df.nunique())
print("\n")

"""
With the distribution of unique values we could notice that there are 4 products that'd been sold to 72 clients.
With 4 quantities and 4 prices, along 100 distinct days
"""

# creating a specific dataframe to see sales attributes correlation
correlation_sales_df = sales_df[["quantity", "unit_price", "client_id", "order_date"]]

# correlation matrix for sales df
correlation_matrix = correlation_sales_df.corr()

# plot correlation heatmap for sales df
plt.figure(figsize=(11, 7))
sns.heatmap(correlation_matrix, annot=True)
plt.show()
"""
With the correlation heatmap we could see that none of the fields have a strong correlation with each other, basically
"""

# create a new sales dataframe to calculate sales and quantity sold by products
sales_per_product_df = sales_df[["product_name", "quantity"]]
sales_per_product_df["sales"] = sales_df.quantity * sales_df.unit_price

# Group sales by products
print("Sales by product:")
print(sales_per_product_df.groupby("product_name").sum())
print("\n")

"""
With the df grouped by products we could notice that the product with more aggregated value is product D, with less quantity,
sold more than any other product. Representing 31.9 % of all sold volume.
"""

# create a new sales dataframe to calculate sales and quantity sold by clients
sales_per_client_df = sales_df[["client_id", "quantity"]]
sales_per_client_df["sales"] = sales_df.quantity * sales_df.unit_price

# Group sales by clients
sales_per_client_df = sales_per_client_df.groupby("client_id").sum()

print("Top 5 clients:")
print(sales_per_client_df.nlargest(5, ["sales"]))
print("\n")

"""
With the df grouped by clients, we could define who where our five best clients in the last period,
this information could be used for a marketing campaign as we could award them to be great clients.
"""

# create a new sales dataframe to calculate sales and quantity sold by order date
sales_per_date_df = sales_df[["order_date", "quantity"]]
sales_per_date_df["sales"] = sales_df.quantity * sales_df.unit_price

# Group sales by order date
sales_per_date_df = sales_per_date_df.groupby("order_date").sum()

print("The 5 days we sold more:")
print(sales_per_date_df.nlargest(5, ["sales"]))
print("\n")

"""
With the df grouped by order dates, we could define where was the days we sold more,
and so, try to reproduce what gets done in the stores in those days, to enable a better average selling operation.
"""

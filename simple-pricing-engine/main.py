import pandas as pd

# Define data dictionaries

customer_data = {
    "customer_id": [1, 2, 3],
    "name": ["John Doe", "Jane Doe", "Alice Smith"],
    "location": ["New York", "Los Angeles", "Chicago"],
    "purchase_history": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
}

supplier_data = {
    "supplier_id": [10, 11, 12],
    "name": ["Acme Inc.", "XYZ Supplies", "ABC Products"],
    "location": ["San Francisco", "Seattle", "Dallas"],
    "product_list": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    "price_list": [[100, 120, 150], [110, 130, 160], [120, 140, 170]],
}

logistic_data = {
    "shipment_id": [100, 101, 102, 103],
    "origin": ["San Francisco", "Seattle", "Dallas", "Florida"],
    "destination": ["New York", "Los Angeles", "Chicago", "Texas"],
    "cost": [50, 60, 70, 90],
}

rfq_customer_data = {
    "rfq_id": [20, 21, 22],
    "customer_id": [1, 2, 3],
    "product_id": [1, 4, 7],
    "quantity": [10, 20, 30],
}

current_price_data = {
    "product_id": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "price": [150, 170, 190, 160, 180, 200, 170, 190, 210],
}

historical_price_data = {
    "product_id": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "date": ["2023-10-26", "2023-10-27", "2023-10-28", "2023-10-29", "2023-10-30", "2023-10-31", "2023-11-01", "2023-11-02", "2023-11-03"],
    "price": [140, 160, 180, 150, 170, 190, 160, 180, 200],
}

# Define profit margin

profit_margin = 0.2

# Convert data dictionaries to Pandas DataFrames

df_customer = pd.DataFrame(customer_data)
df_supplier = pd.DataFrame(supplier_data)
df_logistic = pd.DataFrame(logistic_data)
df_rfq_customer = pd.DataFrame(rfq_customer_data)
df_current_price = pd.DataFrame(current_price_data)
df_historical_price = pd.DataFrame(historical_price_data)

# Merge relevant DataFrames

df_merged = df_rfq_customer.merge(df_customer, on="customer_id").merge(df_current_price, on="product_id")

# Calculate minimum competitor price for each product

df_merged["min_competitor_price"] = df_historical_price.groupby("product_id")["price"].transform("min")

# Calculate optimal price

df_merged["optimal_price"] = (
    df_merged["min_competitor_price"] * (1 - profit_margin)
    + df_merged["price"] * profit_margin
)

# Calculate shipping cost

df_merged = df_merged.merge(
    df_logistic,
    left_on=["location"],
    right_on=["destination"],
)

# Calculate total cost per unit

df_merged["total_cost_per_unit"] = (
    df_merged["optimal_price"]
    + df_merged["cost"] / df_merged["quantity"]
)

# Filter suppliers that can provide the product

# Use pd.concat to join the DataFrames on the 'product_id' column
df_merged = pd.concat([df_merged, df_supplier[["supplier_id", "product_list"]]], axis=1, join="inner")

# Set the 'product_id' for the supplier DataFrame as the index
df_supplier.set_index("product_list", inplace=True)

# Merge on the product_id index
df_merged = df_merged.merge(df_supplier[["supplier_id"]], left_on="product_id", right_index=True)

# Select the supplier with the best offer

df_merged = df_merged.loc[df_merged["total_cost_per_unit"] == df_merged.groupby("product_id")["total_cost_per_unit"].min()]

# Extract relevant information for output

df_output = df_merged[
    [
        "rfq_id",
        "customer_id",
        "product_id",
        "quantity",
        "optimal_price",
        "supplier_id"
    ]
]

# Print output

print(df_output)
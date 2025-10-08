# pandas_tutorial.py
# Run: python pandas_tutorial.py

import pandas as pd

# 1. Create DataFrame from dict
data = {
    "name": ["Alice", "Bob", "Charlie", "Alice", "Bob"],
    "category": ["A", "A", "B", "B", "A"],
    "value": [10, 15, 10, 25, 20],
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

# 2. Basic queries
print("\nRows where name == 'Alice':\n", df[df["name"] == "Alice"])

# 3. Add a new column
df["value_plus_tax"] = df["value"] * 1.05
print("\nWith new column:\n", df)

# 4. GroupBy aggregation
grp = df.groupby("name")["value"].agg(["sum", "mean", "count"]).reset_index()
print("\nGroupBy (value) per name:\n", grp)

# 5. Pivot table
pivot = df.pivot_table(index="name", columns="category", values="value", aggfunc="sum", fill_value=0)
print("\nPivot table (sum by name x category):\n", pivot)

# 6. Read/Write CSV (example; commented)
# df.to_csv("example.csv", index=False)
# df2 = pd.read_csv("example.csv")
# print(df2.head())

import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35, 40, 45, 50],
    'Salary': [50000, 60000, 70000, 80000, 90000, 100000]
}
df = pd.DataFrame(data)

# Filtering data
filtered_df = df[df['Age'] > 30]

# Grouping and aggregating data
grouped_df = df.groupby('Name').agg({'Age': 'mean', 'Salary': 'sum'})

# Printing the results
print("Filtered DataFrame:")
print(filtered_df)
print("\nGrouped and Aggregated DataFrame:")
print(grouped_df)
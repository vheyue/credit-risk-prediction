import pandas as pd

# Example custumer data
data = {
  "age": [25,40,35,52,29],
  "monthly_income": [1500, 3000, 2200, 4200, 1800], 
  "dafault": [0,0,1,0,1]
}
df = pd.DataFrame(data)

print("First rows:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDataset dimensions:")
print(df.shape)

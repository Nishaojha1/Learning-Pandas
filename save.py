import pandas as pd

data = {
    "Name": ["Ram", "shyam","kiaa"],
    "Age": [10, 20, 30],
    "City": ["Maharashtra", "Pune", "Delhi"],
}
df = pd.DataFrame(data)
print(df)
# df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)

import pandas as pd

df = pd.read_excel(r"C:\Users\ZAHEDI\Downloads\employee_data.xlsx")

print("First Five Rows:")
print(df.head())

print("\nMissing Values in Each Column:")
print(df.isnull().sum())

df["Department"] = df["Department"].fillna("Unknown")

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
df["Experience"] = df["Experience"].fillna(df["Experience"].mean())

df["Salary_Level"] = df["Salary"].apply(
    lambda x: "High" if x >= 60000
    else "Medium" if x >= 40000
    else "Low"
)

df = df.drop_duplicates()

print("\nCleaned Employee Data:")
print(df)

df.to_excel(r"C:\Users\ZAHEDI\Downloads\cleaned_employee_data.xlsx", index=False)

print("\nCleaned data successfully exported to Excel!")

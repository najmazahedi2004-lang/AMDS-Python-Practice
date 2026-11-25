
import pandas as pd
import numpy as np
import openpyxl

a = np.array([1, 2, 3])

print(a)
print(type(a))

excel_file = pd.read_excel(
    r"C:\Users\ZAHEDI\Downloads\Test1.xlsx"
)

excel_file.index = excel_file.index + 1

print(excel_file)

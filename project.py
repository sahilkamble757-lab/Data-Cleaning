import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\Sahil Kamble\OneDrive\Desktop\PYTHON CHAPTER ONE\PANDA FOR DATA SCIENCE\project panda file\PANDAS FOR DATASCIENCE\Messy_Employee_dataset.csv")
print(df.head())

#print missing value 
print("missing value in each column")
print(df.isnull().sum())


df['Salary'] = df["Salary"].fillna(df["Salary"].mean())
print(df['Salary'] )

# Fill Age missing with median
print("age filling")
df['Age'] = df['Age'].fillna(df['Age'].median())
print(df['Age'])

#fixing data 
#employr id want in string 
df['Employee_ID'] = df['Employee_ID'].astype(str).str.strip()
df['Join_Date'] = pd.to_datetime(df['Join_Date'] , errors='coerce')

#cleaning phone numbers 
df['Phone'] = df['Phone'].astype(str)
df['Phone'] = df['Phone'].str.replace(r'[^0-9]', '', regex=True)
print(df['Phone'])

#remove duplicates
df.drop_duplicates(inplace=True)

#replace n/a ro 0 and replaces 0 equal salary 
print("replcae n/a with 0")
df['Salary'] = df['Salary'].replace('N/A' , 0)
df['Salary'] = df['Salary'].fillna(0)
print(df['Salary'])

#replace 0 salaries to mean
print("replace 0 salaries to mean")
df['Salary'] = np.where(df['Salary'] <=0 , df['Salary'].mean(),df['Salary'])
print(df['Salary'])

Salary_mean = df['Salary'].mean()
Salary_std = df['Salary'].std()

lower_bound =Salary_mean -(3*Salary_std)
upper_bound =Salary_mean +(3*Salary_std)

#remove rows where salary is too high or too low
df = df[(df['Salary'] >= lower_bound) &(df['Salary']<=upper_bound)]

df.to_csv('cleaned_employee_dataset.csv', index=False)
print('Data cleaning completed saved as cleaned_employee_dataset.csv')
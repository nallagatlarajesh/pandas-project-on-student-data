import pandas as pd 
import numpy as np
import seaborn as sns

data = pd.read_csv(r"C:\Users\Rajesh ARN\Downloads\student-dataset.csv")

print(data.head())
print(data)
print(data.tail())
print(data.shape)
print(data.ndim)
print(data.size)
print(data.describe())
print(data.columns)
print(data.nunique())
print(data["gender"].unique())
print(data.isnull().sum())
student = data.drop(["ethnic.group","latitude","longitude","id"],axis=1)  # to drop redundant data
#to pair plot
#sns.pairplot(student)
numeric_student = student.select_dtypes(include='number')
correlation = numeric_student.corr()
sns.heatmap(correlation, xticklabels=correlation.columns, yticklabels=correlation.columns, annot=True)
sns.relplot(x="sciences.grade",y="language.grade",hue="gender",data=student)

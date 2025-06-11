# Question 1
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv('C:\\New folder\\data_with_indicators1.csv')
print(df)


median_a = df['Rtn..1.Day'].median()
median_b = df['Rtn..1.Day.1'].median()
median_c = df['Rtn..2.Day'].median()


df['Rtn..1.Day'].fillna(median_a)
df['Rtn..1.Day.1'].fillna(median_b)
df['Rtn..2.Day'].fillna(median_c)

# Print the new summary
new_summary=df.info()
print(new_summary)

#1.4

data = {
    'Date': df['Date'],
    'Rtn..1.Day': df['Rtn..1.Day'],
    'Rtn..1.Day.1': df['Rtn..1.Day.1'],
    'Rtn..2.Day': df['Rtn..2.Day'],
    #'Count': df['Count']
}

summary = pd.DataFrame(data)

print(summary.describe())

#1.5
# Reset the index of the "summary" DataFrame
summary.reset_index(inplace=True)

# Display the DataFrame in tabular format
print(summary)

# Display a summary of the new table
print(summary.info())

#1.6
df["Date"]=pd.to_datetime(df["Date"].str.replace('/','-'))
summary['Date']=pd.to_datetime(summary['Date'].str.replace("/","-"))

df["Year"]=df["Date"].dt.year
df['Month']=df['Date'].dt.month
df["Day"]=df["Date"].dt.day

summary["Year"]=summary["Date"].dt.year
summary['Month']=summary['Date'].dt.month
summary["Day"]=summary["Date"].dt.day
print(summary)
print(df)
# print(df.info)
#1.7
# summary['Year'].value_counts().sort_index()


#1,7

plt.figure(figsize=(10, 10))
x=summary.Year.value_counts().index
y=summary.Year.value_counts()
plt.xlabel("YEARS")
plt.ylabel("TOTAL SHARES")
plt.title("Total shares Per year")
plt.xticks(x)
plt.ylim(240,255)
plt.bar(x,y,)
plt.show()

#1.8
x=summary.index
data=summary["Rtn..1.Day.1"]
data2=summary["Rtn..2.Day"]
plt.figure(figsize=(15,10))
plt.plot(x,data,c='b',label="Rtn..1.Day.1",alpha=.5)
plt.plot(x,data2,c='y',label="Rtn..2.Day",alpha=.5)
plt.xlabel("Records")
plt.ylabel("Value")
plt.title("Share value Per Record")
plt.legend()
plt.show()

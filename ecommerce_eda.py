#https://github.com/Jotaherrer/DataAnalysis/tree/master/e_commerce
#https://towardsdatascience.com/data-science-for-e-commerce-with-python-a0a97dd7721d
#Basic Imports
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
import numpy as np
# Read dataset and preview
df = pd.read_csv("e_commerce.csv")
# Exploring data
df.info()
# Count null features in the dataset
df.isnull().sum()
# Replace the null features with 0:
df.fillna(0, inplace=True) # Re-check N/A was replaced with 0.
# Group by User ID:
purchases = df.groupby(['User_ID']).sum().reset_index()
purchases.head()
purchase_by_age = df.groupby('Age')['Purchase'].mean().reset_index()
plt.figure(figsize=(10,6))
plt.plot(purchase_by_age['Age'],purchase_by_age['Purchase'],color='blue', marker='x',lw=4,markersize=18)
plt.grid()
plt.xlabel('Age Group', fontsize=14)
plt.ylabel('Total Purchases in $', fontsize=14)
plt.title('Average Sales distributed by age group', fontsize=16)
plt.show()
plt.hist(purchase_by_age['Purchase'])
# Grouping by gender and age
age_and_gender = df.groupby('Age')['Gender'].count().reset_index()
gender = df.groupby('Gender')['Age'].count().reset_index()
# Plot distribution
plt.figure(figsize=(12,9))
plt.pie(age_and_gender['Gender'], labels=age_and_gender['Age'],autopct='%d%%', colors=['cyan', 'steelblue','peru','blue','yellowgreen','salmon','#0040FF'],textprops={'fontsize': 16})
plt.axis('equal')
plt.title("Age Distribution", fontsize='20')
plt.show()
# Plot gender distribution
plt.figure(figsize=(12,9))
plt.pie(gender['Age'], labels=gender['Gender'],autopct='%d%%', colors=['salmon','steelblue'],textprops={'fontsize': 16})
plt.axis('equal')
plt.title("Gender Distribution", fontsize='20')
plt.show()
# Group by occupation:
occupation = df.groupby('Occupation')['Purchase'].mean().reset_index()
# Plot bar chart with line plot:
sns.set(style="white", rc={"lines.linewidth": 3})
fig, ax1 = plt.subplots(figsize=(12,9))
sns.barplot(x=occupation['Occupation'],y=occupation['Purchase'],color='#004488',ax=ax1)
sns.lineplot(x=occupation['Occupation'],y=occupation['Purchase'],color='salmon',marker="o",ax=ax1)
plt.axis([-1,21,8000,10000])
plt.title('Occupation Bar Chart', fontsize='15')
plt.show()
sns.set()
# Group by product ID
product = df.groupby('Product_ID')['Purchase'].count().reset_index()
product.rename(columns={'Purchase':'Count'},inplace=True)
product_sorted = product.sort_values('Count',ascending=False)
# Plot line plot
plt.figure(figsize=(12,6))
plt.plot(product_sorted['Product_ID'][:10], product_sorted['Count'][:10], linestyle='-', color='green', marker='o',lw=4,markersize=12)
plt.title("Best-selling Products", fontsize='20')
plt.xlabel('Product ID', fontsize='18')
plt.ylabel('Products Sold', fontsize='18')
plt.show()
# Group by Age:
occupation = df.groupby('Age')['Purchase'].mean().reset_index()
# Plot bar chart with line plot:
sns.set(style="white", rc={"lines.linewidth": 3})
fig, ax1 = plt.subplots(figsize=(12,9))
sns.barplot(x=occupation['Age'],y=occupation['Purchase'],color='#004488',ax=ax1)
sns.lineplot(x=occupation['Age'],y=occupation['Purchase'],color='salmon',marker="o",ax=ax1)
plt.ylim([8800, 9600])
plt.title('Purchase vs Age Bar Chart', fontsize='15')
plt.show()
sns.set()
occupation = df.groupby('Gender')['Purchase'].mean().reset_index()
# Plot bar chart with line plot:
sns.set(style="white", rc={"lines.linewidth": 3})
fig, ax1 = plt.subplots(figsize=(8,6))
sns.barplot(x=occupation['Gender'],y=occupation['Purchase'],color='#004488',ax=ax1)
sns.lineplot(x=occupation['Gender'],y=occupation['Purchase'],color='salmon',marker="o",ax=ax1)
plt.ylim([8000, 9600])
plt.title('Purchase vs Gender Bar Chart', fontsize='15')
plt.show()
sns.set()

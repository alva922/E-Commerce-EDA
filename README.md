# E-Commerce-EDA
E-Commerce Exploratory Data Analysis (EDA) Case Study in Python
# Input Data:
df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 550068 entries, 0 to 550067
Data columns (total 12 columns):
 #   Column                      Non-Null Count   Dtype  
---  ------                      --------------   -----  
 0   User_ID                     550068 non-null  int64  
 1   Product_ID                  550068 non-null  object 
 2   Gender                      550068 non-null  object 
 3   Age                         550068 non-null  object 
 4   Occupation                  550068 non-null  int64  
 5   City_Category               550068 non-null  object 
 6   Stay_In_Current_City_Years  550068 non-null  object 
 7   Marital_Status              550068 non-null  int64  
 8   Product_Category_1          550068 non-null  int64  
 9   Product_Category_2          376430 non-null  float64
 10  Product_Category_3          166821 non-null  float64
 11  Purchase                    550068 non-null  int64  
dtypes: float64(2), int64(5), object(5)
memory usage: 50.4+ MB
# Count null features in the dataset
df.isnull().sum()
User_ID                            0
Product_ID                         0
Gender                             0
Age                                0
Occupation                         0
City_Category                      0
Stay_In_Current_City_Years         0
Marital_Status                     0
Product_Category_1                 0
Product_Category_2            173638
Product_Category_3            383247
Purchase                           0
dtype: int64
print(purchase_by_age)
     Age     Purchase
0   0-17  8933.464640
1  18-25  9169.663606
2  26-35  9252.690633
3  36-45  9331.350695
4  46-50  9208.625697
5  51-55  9534.808031
6    55+  9336.280459
# References
https://github.com/Jotaherrer/DataAnalysis/tree/master/e_commerce
https://towardsdatascience.com/data-science-for-e-commerce-with-python-a0a97dd7721d

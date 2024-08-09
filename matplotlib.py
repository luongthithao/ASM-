import matplotlib.pyplot as plt # type: ignore
import pandas as pd

Customer_Data_df = pd.read_csv('Customer_Data_Cleaned_df.csv')
MarketTrend_Data_df = pd.read_csv('MarketTrend_Data_Cleaned_df.csv')
ProductDetail_Data_df = pd.read_csv('ProductDetail_Data_Cleaned_df.csv')
ProductGroup_Data_df = pd.read_csv('ProductGroup_Data_Cleaned_df.csv')
SaleData_df = pd.read_csv('Sale_Data_Cleaned_df.csv')
website_access_category_df = pd.read_csv('website_access_category_Cleaned_df.csv')

Category_Country = Customer_Data_df.groupby('Year')['Count of Category by Country'].sum()

if 'Count of Category' in Customer_Data_df.columns:
    Customer_Data_df['Count of Category'] = Customer_Data_df['Count of Category'].replace('[\$,]', '', regex=True).astype(float)
Count_of_Category_type = Customer_Data_df.groupby('Count of Category')['Count of Category'].sum()
print(Count_of_Category_type)


# Plot the data
if Count_of_Category_type.empty or Count_of_Category_type.isna().all():
        print("No valid numeric data to plot.")
else:
    plt.figure(figsize=(20, 10))
    plt.title('Count of Category by Country')
    plt.xlabel('Country')
    plt.ylabel('Count of Category')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

    import matplotlib.pyplot as plt # type: ignore
import pandas as pd

CustomerData_df = pd.read_csv('CustomerData_Cleaned_df.csv')
MarketTrendData_df = pd.read_csv('MarketTrendData_Cleaned_df.csv')
ProductDetailData_df = pd.read_csv('ProductDetailData_Cleaned_df.csv')
ProductGroupData_df = pd.read_csv('ProductGroupData_Cleaned_df.csv')
SaleData_df = pd.read_csv('SaleData_Cleaned_df.csv')
website_access_category_df = pd.read_csv('website_access_category_Cleaned_df.csv')

Category_Country = CustomerData_df.groupby('Year')['Count of Category by Country'].sum()


if 'Count of Category' in CustomerData_df.columns:
    CustomerData_df['Count of Category'] = CustomerData_df['Count of Category'].replace('[\$,]', '', regex=True).astype(float)
Count_of_Category_type = CustomerData_df.groupby('Count of Category')['Count of Category'].sum()
print(Count_of_Category_type)


# Plot the data
if Count_of_Category_type.empty or Count_of_Category_type.isna().all():
        print("No valid numeric data to plot.")
else:
    plt.figure(figsize=(20, 10))
    plt.title('Count of Category by Country')
    plt.xlabel('Country')
    plt.ylabel('Count of Category')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

#----------------------------------------------------------------

import matplotlib.pyplot as plt # type: ignore
import pandas as pd

Customer_Data_df = pd.read_csv('CustomerData_Cleaned_df.csv')
MarketTrend_Data_df = pd.read_csv('MarketTrendData_Cleaned_df.csv')
ProductDetail_Data_df = pd.read_csv('ProductDetailData_Cleaned_df.csv')
ProductGroup_Data_df = pd.read_csv('ProductGroupData_Cleaned_df.csv')
Sale_Data_df = pd.read_csv('SaleData_Cleaned_df.csv')
website_access_category_df = pd.read_csv('website_access_category_Cleaned_df.csv')


Customer_Data_df['Sum of TotalAmount'] = pd.to_numeric(Customer_Data_df['Sum of TotalAmount'], errors='coerce').fillna(0)
TotalAmount = Customer_Data_df.groupby('Year')['Sum of TotalAmount'].sum()

plt.figure(figsize=(20, 10))
plt.title('Sum of Discount and Sum of TotalAmount by year')
plt.xlabel('Year')
plt.ylabel('Sum of Discount')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#----------------------------------------------------------------

import matplotlib.pyplot as plt # type: ignore
import pandas as pd

Customer_Data_df = pd.read_csv('CustomerData_Cleaned_df.csv')
MarketTrend_Data_df = pd.read_csv('MarketTrendData_Cleaned_df.csv')
ProductDetail_Data_df = pd.read_csv('ProductDetailData_Cleaned_df.csv')
ProductGroup_Data_df = pd.read_csv('ProductGroupData_Cleaned_df.csv')
Sale_Data_df = pd.read_csv('SaleData_Cleaned_df.csv')
website_access_category_df = pd.read_csv('website_access_category_Cleaned_df.csv')

Sale_Data_df = Sale_Data_df.groupby('Year')['Sum of TotalAmount'].sum()


if 'Sum of TotalAmount' in Customer_Data_df.columns:
    Customer_Data_df['Sum of TotalAmount'] = Customer_Data_df['Sum of TotalAmount'].replace('[\$,]', '', regex=True).astype(float)

Count_of_Category_type = CustomerData_df.groupby('Sum of TotalAmount')['Sum of TotalAmount'].sum()
print(Count_of_Category_type)


# Plot the data
if Count_of_Category_type.empty or Count_of_Category_type.isna().all():
        print("No valid numeric data to plot.")
else:
    plt.figure(figsize=(20, 10))
    plt.title('Sum of TotalAmount, Sum of Cost and Sum of Price by year')
    plt.xlabel('Year')
    plt.ylabel('Sum of Cost')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
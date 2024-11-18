# Inventory-Analysis

![home.png](https://github.com/Shaik7981/Inventory-Analysis/blob/main/home.png)

## **Project Objective**

 In this project, the goal is to analyze raw inventory data, clean and transform it, store it in an SQL database, and then create an interactive Power BI dashboard. The dashboard will provide real-time insights into inventory levels, sales performance, and trends, enabling better decision-making and proactive management.

 ---

 ## **Project Structure**

 This project follows a structured approach with the following key steps:

1. **Data Processing**:  
   - Load and clean the Inventory Analysis dataset using Python and pandas.
   - Handle missing data, normalize formats, and ensure data consistency.

2. **SQL Database Setup**:  
   - Create a MySQL database with appropriate tables for each dataset.
   - Load cleaned data into the MySQL tables.
   
3. **Power BI Dashboard**:  
   - Connect Power BI to the MySQL database.
   - Design an interactive dashboard that reflects key sales metrics and updates in real-time.
     
4. **Real-Time Data Updates**:  
   - Configure Power BI to automatically refresh data at intervals or trigger updates based on SQL changes.
     
---

## **Project Steps**

### 1. Dataset Processing

- **Python Script**: `Data_cleaning (1)`  
  The `Data_cleaning (1)` script handles reading, cleaning, and preprocessing CSV files using the pandas library. This step ensures data consistency before loading into the SQL database.
**Example:**
```python
import pandas as pd

# Load Inventory data
df = pd.read_csv('2017PurchasePricesDec.csv')
df1 = pd.read_csv('SalesFINAL12312016.csv')
df2 = pd.read_csv('PurchasesFINAL12312016.csv')
df3 = pd.read_csv('InvoicePurchases12312016.csv')
df4 = pd.read_csv('EndInvFINAL12312016.csv')
df5 = pd.read_csv('BegInvFINAL12312016.csv')

# Clean and preprocess Sales data
df2 = df2.dropna()
df3 = df3.dropna()
df4 = df4.dropna()
df5 = df5.dropna()

# Export cleaned data
df.to_csv("2017PurchasePricesDec.csv", index = False)
df1.to_csv("cleaned_SalesFinal",index = False)
df2.to_csv("cleaned_PurchaseFinal1",index= False)
df3.to_csv('InvoicePurchases12312016.csv', index = False)
df4.to_read_csv('EndInvFINAL12312016.csv', index = False)
df5.to_csv('BegInvFINAL12312016.csv', index = False)
```

---

### 2. SQL Database Integration

- **SQL Setup Script**: `Digital_explorers_041.sql`  
  This script creates the necessary tables in MySQL for storing the cleaned data. Ensure you have MySQL Workbench or an equivalent setup.

---

### 3. Power BI Dashboard

- **Power BI File**: `Digital Explorers.pbix`  
  This file contains an interactive, real-time dashboard built in Power BI. The dashboard includes visualizations like:

  - **Month wise Sales**: A bar chart showing sales of inventory for Every Month.
  - **Month Wise Purchases**: A line chart tracking Puchase of inventory for Every Month.
  - **Average Purchases Cost of Inventory**: A KPI card comparing the cost of each product.
  
**Power BI Setup**:
1. Connect Power BI to the MySQL database:
   - Go to "Get Data" > "MySQL Database".
   - Enter your database connection details and load the tables.
2. Create dynamic visualizations using sales and product data.
3. Enable automatic refresh to update the dashboard in real-time.

https://github.com/Shaik7981/Inventory-Analysis/blob/main/purchase%20Dash%20board.png

![https://github.com/Shaik7981/Inventory-Analysis/blob/main/Sales%20dashboard.png)

 

  
  


  

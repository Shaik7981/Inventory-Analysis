# Inventory-Analysis

![home.png](https://github.com/Shaik7981/Inventory-Analysis/blob/main/home.png)

## **Project Objective**

 In this project, the goal is to analyze raw inventory data, clean and transform it, store it in an SQL database, and then create an interactive Power BI dashboard. The dashboard will provide real-time insights into inventory levels, sales performance, and trends, enabling better decision-making and proactive management.

 ---

 ## **Project Structure**

 This project follows a structured approach with the following key steps:

1. **Data Processing**:  
   - Load and clean the Adventure Works dataset using Python and pandas.
   - Handle missing data, normalize formats, and ensure data consistency.

2. **SQL Database Setup**:  
   - Create a MySQL database with appropriate tables for each dataset (Product, Sales, Region, etc.).
   - Load cleaned data into the MySQL tables.
   
3. **Power BI Dashboard**:  
   - Connect Power BI to the MySQL database.
   - Design an interactive dashboard that reflects key sales metrics and updates in real-time.
   - 
4. **Real-Time Data Updates**:  
   - Configure Power BI to automatically refresh data at intervals or trigger updates based on SQL changes.
   - 
---

## **Project Steps**

### 1. Dataset Processing

- **Python Script**: `data_processing.py`  
  The `data_processing.py` script handles reading, cleaning, and preprocessing CSV files using the pandas library. This step ensures data consistency before loading into the SQL database.

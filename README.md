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

![purchase Dash board.png](https://github.com/Shaik7981/Inventory-Analysis/blob/main/purchase%20Dash%20board.png)

![Sales dashboard.png](https://github.com/Shaik7981/Inventory-Analysis/blob/main/Sales%20dashboard.png)

---

### 4. Real-Time Data Updates

Configure Power BI to refresh the data either at scheduled intervals or based on SQL triggers.

- **Auto Refresh**:
  - Set a refresh interval in Power BI (e.g., every 15 minutes).
  - Use SQL triggers to push updates when significant changes occur in the data.

---

## **Folder Structure**

```
B40 Project/
│
├── data/
│   ├── 2017PurchasePricesDec.csv
│   ├── BegInvFINAL12312016.csv
│   ├── EndInvFINAL12312016.csv
│   ├── InvoicePurchases12312016.csv
│   ├── PurchasesFINAL12312016.csv
│   ├── SalesFINAL12312016.csv

│
├── scripts/
│   ├── Data_cleaning (1).py
│   ├── Digital_explorers_041.sql
│
├── dashboard/
│   ├── Digital Explorers.pbix
│
├── README.md
├── Screenshot.png
```

---

## **Prerequisites**

- **Python**: Install pandas and MySQL connector (`pip install pandas mysql-connector-python`).
- **MySQL Database**: Install and configure MySQL Workbench.
- **Power BI**: Download and install Power BI Desktop.

---

## **How to Run the Project**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/Inventory Analysis .git
   ```

2. **Data Cleaning**:
   - Navigate to the `scripts/` folder and run the `Data_cleaning (1).py` script to clean the dataset.
   ```bash
   python Data_cleaning (1).py
   ```

3. **Set Up MySQL Database**:
   - Run the `Digital_explorers_041.sql` script to create the database and tables.
   ```bash
   mysql -u username -p < Digital_explorers_041 .sql
   ```

4. **Load Data into SQL**:
   - Load the cleaned data into the SQL database using MySQL Workbench or command line.

5. **Power BI Dashboard**:
   - Open `Digital Explorers.pbix` in Power BI Desktop.
   - Ensure the data connection is configured to your SQL database.
   - Set up automatic refresh for real-time data updates.

---
 
## **Contributing**

Feel free to submit issues or contribute to the project by creating pull requests. Check the `CONTRIBUTING.md` for guidelines.

---


  
  


  

import warnings

warnings.filterwarnings('ignore')

from sqlalchemy import  create_engine

import pandas as pd

engine = create_engine("mysql+mysqldb://root:1234@127.0.0.1:3306/Inventory_Analysis")

# {root}:{password}@host:port/{database name}

#Establish a connection

conn = engine.connect()

#Read data from CSV into a Pandas DataFrame
data = pd.read_csv("cleaned_PurchaseFinal1.xls")
data1 = pd.read_csv("cleaned_SalesFinal.xls")
data2 = pd.read_csv("Cleaned_PurchasePricesDec.csv")
data3 = pd.read_csv("Cleaned_InvoicePurchases12312016.csv")
data4 = pd.read_csv("Cleaned_EndinvFINAL12312016.csv")
data5 = pd.read_csv("Cleaned_BeginvFINAL12312016.csv")
#Write DataFrame to a SQL table

data.to_sql('Purchase_Final1', engine, index=False, if_exists='replace')
data1.to_sql('sales_Final', engine, index=False, if_exists='replace')
data3.to_sql('Invoice_Purchases', engine, index=False, if_exists='replace')
data2.to_sql('Purchase_PricesDec', engine, index=False, if_exists='replace')
data4.to_sql('Endinv_FINAL', engine, index=False, if_exists='replace')
data5.to_sql('Beginv_FINAL', engine, index=False, if_exists='replace')

#Close Connection
conn.close()
CREATE DATABASE Inventory_Analysis;

USE Inventory_Analysis;


# Profit for each sales
SELECT p.PurchasePrice, s.SalesPrice, (s.SalesPrice - p.PurchasePrice) AS Profit
FROM Sales_final AS s 
LEFT JOIN Purchase_final1 AS p
ON s.InventoryId = p.InventoryID;

# Wiewing the datat

SELECT *
FROM beginv_final;

SELECT *
FROM endinv_final;

SELECT *
FROM invoice_purchases;

SELECT *
FROM Purchase_final1;

SELECT *
FROM purchase_pricesdec;

SELECT *
FROM sales_final;




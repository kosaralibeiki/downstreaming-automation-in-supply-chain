import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kowsar.1995",
    database="supply_chain"
)

cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS items (
    item_id INT PRIMARY KEY,
    item_number VARCHAR(50),
    description VARCHAR(255),
    category VARCHAR(100)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS warehouses (
    warehouse_id INT PRIMARY KEY,
    name VARCHAR(100),
    location VARCHAR(255)
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS inventory (
    inventory_id INT PRIMARY KEY,
    item_id INT,
    warehouse_id INT,
    quantity INT,
    
    FOREIGN KEY (item_id) REFERENCES items(item_id),
    FOREIGN KEY (warehouse_id) REFERENCES warehouses(warehouse_id)
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS forecasts (
    forecast_id INT PRIMARY KEY,
    item_id INT,
    warehouse_id INT,
    forecasted_quantity INT,

    FOREIGN KEY (item_id) REFERENCES items(item_id),
    FOREIGN KEY (warehouse_id) REFERENCES warehouses(warehouse_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS distribution_orders (
    DO_id INT PRIMARY KEY,
    item_id INT,
    source_warehouse_id INT,
    destination_warehouse_id INT,
    quantity INT,
    type VARCHAR(50),
    
    FOREIGN KEY (item_id) REFERENCES items(item_id),
    FOREIGN KEY (source_warehouse_id) REFERENCES warehouses(warehouse_id),
    FOREIGN KEY (destination_warehouse_id) REFERENCES warehouses(warehouse_id)
)
""")

connection.commit()

print("Items table created successfully.")
print("Warehouses table created successfully.")
print("Inventory table created successfully.")
print("Forecasts table created successfully.")
cursor.close()
connection.close()
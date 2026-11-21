from multiprocessing.dummy import connection

import mysql.connector
from data_loader import generate_distribution_orders, generate_items, generate_warehouses, generate_inventory, generate_forecasts, generate_sales


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Kowsar.1995",
        database="supply_chain"
    )



def create_tables():
    connection = get_connection()
    cursor = connection.cursor() 


    cursor.execute("SHOW TABLES LIKE 'warehouses'")
    result = cursor.fetchone()
    if result is not None:
        print("Warehouse table already exists. Skipping table creation.")
    else:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS warehouses (
            warehouse_id INT PRIMARY KEY,
            name VARCHAR(100),
            location VARCHAR(255)
        )
        """)
        print("Warehouses table created successfully.")


    cursor.execute("SHOW TABLES LIKE 'items'")
    result = cursor.fetchone()

    if result is not None:
        print("Item table already exists. Skipping table creation.")
    else:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            item_id INT PRIMARY KEY,
            item_number VARCHAR(50),
            description VARCHAR(255),
            category VARCHAR(100),
            main_WH INT

            FOREIGN KEY (main_WH) REFERENCES warehouses(warehouse_id)
        )
        """)
        print("Items table created successfully.")  


    cursor.execute("SHOW TABLES LIKE 'inventory'")
    result = cursor.fetchone()
    if result is not None:
        print("Inventory table already exists. Skipping table creation.")
    else:
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
        print("Inventory table created successfully.")


    cursor.execute("SHOW TABLES LIKE 'forecasts'")
    result = cursor.fetchone()
    if result is not None:
        print("Forecasts table already exists. Skipping table creation.")
    else:
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
        print("Forecasts table created successfully.")


    cursor.execute("SHOW TABLES LIKE 'distribution_orders'")
    result = cursor.fetchone()
    if result is not None:
        print("Distribution orders table already exists. Skipping table creation.")
    else:
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
        print("Distribution orders table created successfully.")


    
    cursor.execute("SHOW TABLES LIKE 'sales'")
    result = cursor.fetchone()
    if result is not None:
        print("Sales table already exists. Skipping table creation.")
    else:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            sale_id INT PRIMARY KEY,
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
        print("Sales table created successfully.")

    connection.commit()
    cursor.close()
    connection.close()



def insert_generated_data():
    connection = get_connection()
    cursor = connection.cursor()

    items = list(generate_items())
    warehouses = list(generate_warehouses())
    inventory = generate_inventory(items, warehouses)
    forecasts = generate_forecasts(items, warehouses)
    distribution_orders = generate_distribution_orders(items, warehouses)
    sales = generate_sales(items, warehouses)


    cursor.execute("SELECT COUNT(*) FROM items")
    count = cursor.fetchone()[0]
    if count > 0:
        print("Data already exists in the items table. Skipping data insertion.")
        
    else:
        for item in items:
                cursor.execute("""
                INSERT INTO items (item_id, item_number, description, category, main_WH)
                VALUES (%s, %s, %s, %s, %s)""",
                (item['item_id'], item['item_number'], item['description'], item['category'], item['main_WH'])
                )


    cursor.execute("SELECT COUNT(*) FROM warehouses")
    count = cursor.fetchone()[0]
    if count > 0:
        print("Data already exists in the warehouses table. Skipping data insertion.")
        
    else:   
        for warehouse in warehouses:
            cursor.execute("""
            INSERT INTO warehouses (warehouse_id, name, location)
            VALUES (%s, %s, %s)""",
            (warehouse['warehouse_id'], warehouse['name'], warehouse['location'])
            )

    cursor.execute("SELECT COUNT(*) FROM inventory")
    count = cursor.fetchone()[0]
    if count > 0:
        print("Data already exists in the inventory table. Skipping data insertion.")
        
    else:
        for inv in inventory:
            cursor.execute("""
            INSERT INTO inventory (inventory_id, item_id, warehouse_id, quantity)
            VALUES (%s, %s, %s, %s)""",
        (inv['inventory_id'], inv['item_id'], inv['warehouse_id'], inv['quantity'])
        )

    cursor.execute("SELECT COUNT(*) FROM forecasts")
    count = cursor.fetchone()[0]
    if count > 0:
        print("Data already exists in the forecasts table. Skipping data insertion.")
        
    else:
        for forecast in forecasts:
            cursor.execute("""
            INSERT INTO forecasts (forecast_id, item_id, warehouse_id, forecasted_quantity)
            VALUES (%s, %s, %s, %s)""",
            (forecast['forecast_id'], forecast['item_id'], forecast['warehouse_id'], forecast['forecasted_quantity'])
            )

    cursor.execute("SELECT COUNT(*) FROM distribution_orders")
    count = cursor.fetchone()[0]
    if count > 0:
        print("Data already exists in the distribution_orders table. Skipping data insertion.")
        
    else:
        for do in distribution_orders:
            cursor.execute("""
            INSERT INTO distribution_orders (DO_id, item_id, source_warehouse_id, destination_warehouse_id, quantity, type)
            VALUES (%s, %s, %s, %s, %s, %s)""",
            (do['DO_id'], do['item_id'], do['source_warehouse_id'], do['destination_warehouse_id'], do['quantity'], do['type'])
            )

    cursor.execute("SELECT COUNT(*) FROM sales")
    count = cursor.fetchone()[0]
    if count > 0:
        print("Data already exists in the sales table. Skipping data insertion.")
        
    else:
        for sale in sales:
            cursor.execute("""
            INSERT INTO sales (sale_id, item_id, warehouse_id, quantity_sold, sale_date)
            VALUES (%s, %s, %s, %s, %s)""",
            (sale['sale_id'], sale['item_id'], sale['warehouse_id'], sale['quantity_sold'], sale['sale_date'])
            )

    connection.commit()
    cursor.close()
    connection.close()



create_tables()
insert_generated_data()
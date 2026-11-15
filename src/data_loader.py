import random
from faker import Faker

fake = Faker()


categories = [
    "Inserts",
    "Round tools",
    "Cutting tools",
    "Measuring tools"]


def generate_items(count=20):
    for i in range(1, count + 1):
        item = {
            "item_id": i,
            "item_number": f"1{i:05d}",
            "description": f"DESC-{i:05d}",
            "category": random.choice(categories)
        }

        yield item

def generate_warehouses(count=3):
    for i in range(1, count + 1):
        warehouse = {
            "warehouse_id": i,
            "name": f"Warehouse-{i:03d}",
            "location": fake.country()
        }

        yield warehouse

def generate_inventory(items, warehouses):
    inventory_id = 1
    for item in items:
        for warehouse in warehouses:
            inventory = {
                "inventory_id": inventory_id,
                "item_id": item['item_id'],
                "warehouse_id": warehouse['warehouse_id'],
                "quantity": random.randint(0, 1000)
            }

            yield inventory
            inventory_id += 1


def generate_forecasts(items, warehouses):
    forcast_id = 1
    for item in items:
        for warehouse in warehouses:
            forecast = {
                "forecast_id": forcast_id,
                "item_id": item['item_id'],
                "warehouse_id": warehouse['warehouse_id'],
                "forecasted_quantity": random.randint(0, 1000)
            }

            yield forecast
            forcast_id += 1


def generate_distribution_orders(items, warehouses):
    do_id = 1
    for item in items:
        source_warehouse = random.choice(warehouses)
        destination_warehouse = random.choice([w for w in warehouses if w != source_warehouse])
        distribution_order = {
            "DO_id": do_id,
            "item_id": item['item_id'],
            "source_warehouse_id": source_warehouse['warehouse_id'],
            "destination_warehouse_id": destination_warehouse['warehouse_id'],
            "item_id": item['item_id'],
            "source_warehouse_id": source_warehouse['warehouse_id'],
            "destination_warehouse_id": destination_warehouse['warehouse_id'],
            "quantity": random.randint(0, 1000),
            "type": random.choice(["Type A", "Type B", "Type C"])
        }

        yield distribution_order
        do_id += 1
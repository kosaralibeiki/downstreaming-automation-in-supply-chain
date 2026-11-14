from src.data_loader import generate_distribution_orders, generate_items, generate_warehouses, generate_inventory, generate_forecasts

def test_generate_items():
    items = list(generate_items())
    assert len(items) == 20
    assert all("item_id" in item and "item_number" in item and "description" in item and "category" in item for item in items)


def test_generate_warehouses():
    warehouses = list(generate_warehouses())
    assert len(warehouses) == 3
    assert all("warehouse_id" in warehouse and "name" in warehouse and "location" in warehouse for warehouse in warehouses)



def test_generate_inventory():
    items = list(generate_items())
    warehouses = list(generate_warehouses())
    inventory = list(generate_inventory(items, warehouses))
    assert len(inventory) == len(items) * len(warehouses)
    assert all("inventory_id" in inv and "item_id" in inv and "warehouse_id" in inv and "quantity" in inv for inv in inventory)

def test_generate_forecasts():
    items = list(generate_items())
    warehouses = list(generate_warehouses())
    forecasts = list(generate_forecasts(items, warehouses))
    assert len(forecasts) == len(items) * len(warehouses)
    assert all("forecast_id" in forecast and "item_id" in forecast and "warehouse_id" in forecast and "forecasted_quantity" in forecast for forecast in forecasts)


def test_generate_distribution_orders():
    items = list(generate_items())
    warehouses = list(generate_warehouses())
    distribution_orders = list(generate_distribution_orders(items, warehouses))
    assert len(distribution_orders) > 0
    assert all("DO_id" in order and "item_id" in order and "source_warehouse_id" in order and "destination_warehouse_id" in order and "quantity" in order and "type" in order for order in distribution_orders)



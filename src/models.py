# data models for the application

class Item:
    def __init__(self, item_id: int, item_number: str, description: str, category: str):
        self.item_id = item_id
        self.item_number = item_number
        self.description = description
        self.category = category

    def __repr__(self):
        return f"Item(item_id={self.item_id}, item_number={self.item_number}, description={self.description}, category={self.category})"



class Warehouse:
    def __init__(self, warehouse_id: int, name: str, location: str):
        self.warehouse_id = warehouse_id
        self.name = name
        self.location = location

    def __repr__(self):
        return f"Warehouse(warehouse_id={self.warehouse_id}, name={self.name}, location={self.location})"




    class Inventory:
        def __init__(self, inventory_id: int, item_id: int, warehouse_id: int, quantity: int):
            self.inventory_id = inventory_id
            self.item_id = item_id
            self.warehouse_id = warehouse_id
            self.quantity = quantity

        def __repr__(self):
            return f"Inventory(inventory_id={self.inventory_id}, item_id={self.item_id}, warehouse_id={self.warehouse_id}, quantity={self.quantity})"



    class Forecast:
        def __init__(self, forecast_id: int, item_id: int, warehouse_id: int, forecasted_quantity: int):
            self.forecast_id = forecast_id
            self.item_id = item_id
            self.warehouse_id = warehouse_id
            self.forecasted_quantity = forecasted_quantity

        def __repr__(self):
            return f"Forecast(forecast_id={self.forecast_id}, item_id={self.item_id}, warehouse_id={self.warehouse_id}, forecasted_quantity={self.forecasted_quantity})"
        

    class Distribution_order:
        def __init__(self, DO_id: int, item_id: int, warehouse_id: int, quantity: int, typre: str):
            self.DO_id = DO_id
            self.item_id = item_id
            self.warehouse_id = warehouse_id
            self.quantity = quantity
            self.type = type

        def __repr__(self):
            return f"DistributionOrder(DO_id={self.DO_id}, item_id={self.item_id}, warehouse_id={self.warehouse_id}, quantity={self.quantity}, type={self.type})"
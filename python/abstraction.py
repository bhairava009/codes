from abc import ABC, abstractmethod

class Dish(ABC):
    def __init__(self, name, price):
        self._name = name
        self._price = price
    
    @abstractmethod
    def prepare_dish(self):
        pass

    @abstractmethod
    def get_ingredients(self):
        pass

    def server_dish(self):
        return "Serving dish :", {self._name}

    def get_name(self):
        return "Dish Name : ", {self._name}
    
    def get_price(self):
        return "Dish Price : ", {self._price}
    

class Pizza(Dish):
    def __init__(self, name, price):
        super().__init__(name, price)

    def prepare_dish(self):
        return f"{self._name} is getting prepared"
    
    def get_ingredients(self):
        return f"Ingredients : Water, Floor-dough, Toppings"

class Restaurant:
    def order_dish(self, dish:Dish):
        if dish:
            print("Customer Ordered ", dish.get_name(), "whoes price is ", dish.get_price())
            dish.get_ingredients()
            dish.prepare_dish()
            dish.server_dish()
        else:
            print("That Dish is currently Un-available")

# Declaring an Restaurant Object
lpu_restu = Restaurant()

FarmHouse = Pizza("FarmHouse", 250)

lpu_restu.order_dish(FarmHouse)
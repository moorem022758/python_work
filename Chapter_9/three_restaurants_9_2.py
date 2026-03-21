# 9-2 three restaurants

class Restaurant:
    
    def __init__(self, restaurant_name, restaurant_type):
        """Initialization of restaurant_name and restaurant_type"""
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type
        
    def describe_restaurant(self):
        """describ_restaurant() method creation"""
        print(f"\n{self.restaurant_name}, {self.restaurant_type}")
        
    
    def open_restaurant(self):
        """open_restaurant() method creation"""
        print(f"\n{self.restaurant_name} a {self.restaurant_type}\
 eatery that is currently open. ")
        
        
"""First Instance call"""
restaurant = Restaurant('Kudos', 'Mexican')
restaurant.describe_restaurant()
restaurant.open_restaurant()

"""Second Instance call"""
restaurant_1 = Restaurant('KFC', 'Poultry')
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

"""Third Instance call"""
restaurant_2 = Restaurant('Hardee', 'Burger')
restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()
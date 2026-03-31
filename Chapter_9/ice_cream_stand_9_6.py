# 9-6 Ice Cream Stand

class Restaurant:
    
    def __init__(self, restaurant_name, restaurant_type):
        """Initialization of restaurant_name and restaurant_type"""
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type
        
    def describe_restaurant(self):
        """describ_restaurant() method creation"""
        print(f"{self.restaurant_name}, {self.restaurant_type}")
        
    
    def open_restaurant(self):
        """open_restaurant() method creation"""
        print(f"{self.restaurant_name} a {self.restaurant_type}\
 eatery that is currently open. ")
        
        
class IceCreamStand:
    def __init__(self, flavors):
        """Initialization of flavors"""
        self.flavor_type = flavors
        
    def display_flavors(self):
        print(f"{self.flavor_type} is one of our flavors.")
        
        

restaurant = Restaurant('Kudos', 'Mexican')
restaurant.describe_restaurant()
restaurant.open_restaurant()
iceream = IceCreamStand('almonds')
iceream.display_flavors()
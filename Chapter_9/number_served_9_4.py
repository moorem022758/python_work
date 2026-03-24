# Number Served

class Restaurant:
    
    def __init__(self, restaurant_name, restaurant_type, number_served=0):
        """Initialization of restaurant_name and restaurant_type"""
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type
        self.number_served = number_served
        
    def describe_restaurant(self):
        """describ_restaurant() method creation"""
        print(f"{self.restaurant_name}, {self.restaurant_type}")
        
    
    def open_restaurant(self):
        """open_restaurant() method creation"""
        print(f"{self.restaurant_name} a {self.restaurant_type}\
 eatery that is currently open. ")

    def print_number_served(self):
        """Print the number of customers served."""
        print(f"Number served: {self.number_served}")
        
    # def set_number_served(self):
        # """set a new number served value."""
        # New_number_served = input("How many have been served")
        # print(f"New Number served: {New_number_served}")
        
    def Increment_number_served(self):
        """Increment the number of customers who have been served"""
        full_number_served = self.number_served + 100
        print(f"Full number served: {full_number_served}")
        
    
restaurant = Restaurant('Kudos', 'Mexican', 10)
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.print_number_served()
# restaurant.set_number_served()
restaurant.Increment_number_served()




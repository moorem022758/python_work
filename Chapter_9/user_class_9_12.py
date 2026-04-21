# Module for User Class

"""Module for User class"""

class User:
    def __init__(self, first_name, last_name):
        """Initialize User class first_name and Last_name"""
        self.first_name = first_name
        self.last_name = last_name
        
    def describe_user(self):
        """describe_user () method creation"""
        print(f"Here is the users infomation - {self.first_name} \
{self.last_name}")
        
    def greet_user(self):
        """greet_user () method creation"""
        print(f"Hello {self.first_name} {self.last_name}")
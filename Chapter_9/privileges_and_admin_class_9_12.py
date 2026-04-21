# Module for Privileges and admin class


from user_class_9_12 import User

"""Module containing the Privileges and Admin Class"""

class Admin(User):
    def __init__(self, first_name, last_name, privileges = ['can add post',\
        'can delete post', 'can ban user']):
        super().__init__(first_name, last_name)
        self.privileges = Privileges(privileges)
        
    def show_privileges(self):
        print(f"list of administrator's set of privileges. {self.privileges}")
        
        
class Privileges():
    def __init__(self, privileges = ['can add post', 'can delete post',\
        'can ban user']):
        """Initialize privileges call attribute"""
        self.privileges = privileges
        
    def show_privileges(self):
        print(f"List of administrator's set of privileges. {self.privileges}")
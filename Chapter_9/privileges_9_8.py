# 9-8 Privilesges

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
    
    
        

"""First Instance call"""        
# user_profile = User('Michael', 'Moore')
# user_profile.describe_user()
# user_profile.greet_user()

"""Second Instance call"""
# user_profile_1 = User('Harold', 'Moore')
# user_profile_1.describe_user()
# user_profile_1.greet_user()

"""Third Instance call"""
# user_profile_2 = User('Robert', 'Moore')
# user_profile_2.describe_user()
# user_profile_2.greet_user()

""""9_7_admin Instance call"""
# admin_rights = Admin('John', 'Doe')
# admin_rights.privileges.show_privileges()



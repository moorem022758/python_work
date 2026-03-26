# 9-5 Login Attempts

class User:
    def __init__(self, first_name, last_name, login_attempts):
        """Initialize User class first_name and Last_name"""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts
        
    def describe_user(self):
        """describe_user () method creation"""
        print(f"Here is the users infomation - {self.first_name} \
{self.last_name}")
        
    def greet_user(self):
        """greet_user () method creation"""
        print(f"Hello {self.first_name} {self.last_name}")
        
    def increment_login_attempts(self):
        """increment_login_attempts () method creation"""
        add_logins = self.login_attempts + 1
        print(f"{add_logins}")
        
    def reset_login_attempts(self):
        """reset_login_attempts () method creation"""
        self.login_attempts = 0
        print(f"Login attempts reset to {self.login_attempts}")
        

"""First Instance call"""        
user_profile = User('Michael', 'Moore', 0)
user_profile.describe_user()
user_profile.greet_user()

"""Second Instance call"""
user_profile_1 = User('Harold', 'Moore', 0)
user_profile_1.describe_user()
user_profile_1.greet_user()

"""Third Instance call"""
user_profile_2 = User('Robert', 'Moore', 0)
user_profile_2.describe_user()
user_profile_2.greet_user()

"""Login_attempts Instance call"""
attemps = User('Maurice', 'Moore', 0)
attemps.increment_login_attempts()
attemps.increment_login_attempts()
attemps.reset_login_attempts()

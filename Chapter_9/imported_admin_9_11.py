# Import Admin 9-11

"""Importing Admin class from module and call the show_privileges()"""
from privileges_9_8 import Admin

"""Instance Call"""
my_admin = Admin('arthur', 'moore',)
my_admin.privileges.show_privileges()

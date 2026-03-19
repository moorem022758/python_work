# Put the functions for the example printing_models.py in a separate file
# called print_functions.py. Write in import statement at the top of 
# printing_models.py and modify the file to use the imported functions.


"""Reorganize the code above into two funcstions"""
def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left"""
    """move each design to completed_models after printing"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Print model: {current_design}")
        completed_models.append(current_design)
        
def show_completed_models(completed_models):
    """show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
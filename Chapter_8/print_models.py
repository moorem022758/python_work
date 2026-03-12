# Modifying a List in a function

"""Start with some designs that need to be printed"""
unprinted_design = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

"""simulate printing each design, until noe are left"""
"""Move each design to completed_models after print"""
while unprinted_design:
    current_design = unprinted_design.pop()
    print(f"print model: {current_design}")
    completed_models.append(current_design)
    
    
"""Display all completed models."""
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
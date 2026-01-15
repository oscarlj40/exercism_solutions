"""Functions used in preparing Guido's gorgeous lasagna."""

EXPECTED_BAKE_TIME = 40        # Total expected baking time
PREPARATION_TIME = 2           # Time for layer

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining."""
    return EXPECTED_BAKE_TIME - elapsed_bake_time
    
def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time based on number of layers."""
    return PREPARATION_TIME * number_of_layers
    
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate total time spent cooking so far."""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
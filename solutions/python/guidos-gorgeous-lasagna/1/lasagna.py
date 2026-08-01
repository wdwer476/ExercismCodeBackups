EXPECTED_BAKE_TIME = 40


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): Time already spent baking (in minutes).

    Returns:
        int: The number of minutes remaining to bake, calculated as the
        difference between the total expected bake time and the elapsed
        bake time.

    This function takes an integer representing the time already spent
    baking and subtracts it from the expected bake time to determine
    how many minutes of baking time remain.

    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(layers):
    """Calculate the preparation time in minutes.

    Parameters:
        layers (int): The number of layers in the lasagna.

    Returns:
        int: The total preparation time in minutes, based on 2 minutes
        per layer.

    This function takes an integer representing the number of layers
    in the lasagna and multiplies it by 2, since each layer takes
    an average of 2 minutes to prepare.

    """
    return layers * 2


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): Time the lasagna has been baking in the oven.

    Returns:
        int: The total time elapsed (in minutes) preparing and baking.

    This function takes two integers representing the number of lasagna
    layers and the time already spent baking the lasagna. It calculates
    the total elapsed minutes spent cooking (preparing + baking).

    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
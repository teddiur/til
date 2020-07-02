MIN_DRIVING_AGE = 18


def allowed_driving(name, age):
    """Print '{name} is allowed to drive' or '{name} is not allowed to drive'
       checking the passed in age against the MIN_DRIVING_AGE constant"""
    allowed = ''
    n_allowed = 'not '
    print(f'{name} is {allowed if age >= MIN_DRIVING_AGE else n_allowed}allowed to drive')
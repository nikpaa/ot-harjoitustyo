class CalculatorError(Exception):
    """ Custom error class for all the errors that the calculator raises
    """
    def __init__(self, message):
        self.message = message

# CalculationErrorException: Custom Exception Class whenever there are calculation errors
class CalculationErrorException(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)
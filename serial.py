class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self,start=100):
        """Initialize Serial Generator"""
        self.start = start - 1
        self.serial = start - 1

    def generate(self):
        """Increment serial number by 1, starting at start"""
        self.serial += 1
        return self.serial

    def reset(self):
        """Reset serial number to start value"""
        self.serial = self.start




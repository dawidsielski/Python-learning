"""
Learning how to log
"""
import logging

logging.basicConfig(filename="logging_basics.log", level=logging.INFO,
                    format="%(asctime)s:%(funcName)s:%(message)s")

def add(a_value, b_value):
    """Function takes two argument a and b and returns the sum a + b"""
    logging.info("Function run with argments %i and %i", a_value, b_value)
    return a_value + b_value

def multiply(a_value, b_value):
    """Function takes two argument a and b and returns the multiplication a * b"""
    logging.info("Function run with argments %i and %i", a_value, b_value)
    return a_value * b_value

def main():
    """Function prepared for testing purposes"""
    for a_value, b_value in enumerate(range(100000)):
        add(a_value, b_value)
        multiply(a_value, b_value)

if __name__ == "__main__":
    main()

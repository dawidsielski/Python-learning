def check_decimal(number):
    import re
    print(bool(re.search(r'^\d+(\.\d{1,2})?$', number)))


check_decimal("12.233")
check_decimal("12.23")
check_decimal("12.2")
check_decimal("12.")
check_decimal("12")
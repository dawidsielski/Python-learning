"""line 1566"""

def function(n):
    if n == 0:
        return 0
    else:
        return function(n - 1) + 100

print(function(5))
"""
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

  format_duration(62)    # returns "1 minute and 2 seconds"
  format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
Note that spaces are important.
"""
def format_duration(seconds):
    pass





print(format_duration(1) == "1 second")
print(format_duration(62) == "1 minute and 2 seconds")
print(format_duration(120) == "2 minutes")
print(format_duration(3600) == "1 hour")
print(format_duration(3662) == "1 hour, 1 minute and 2 seconds")
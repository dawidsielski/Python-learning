"""line 1417"""
import re

message = "john@google.com"

email_pattern = "(\w+)@((\w+\.)+(com))"
user = re.match(email_pattern, message)
print(user.group(1))

empty = []
filled = [1,2,3]

def if_empty(items):
    if not items:
        print("List is empty.")
    else:
        print("List is not empty.")
        
if_empty(empty)
if_empty(filled)
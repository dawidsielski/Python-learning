def p_decorate(function_name):
    def wrapper():
        return "<p>{}</p>".format(function_name())
    return wrapper

def strong_decorate(function_name):
    def wrapper():
        return "<strong>{}</strong>".format(function_name())
    return wrapper


@strong_decorate
@p_decorate
def my_text():
    return "Lorem Ipsum"


print(my_text())
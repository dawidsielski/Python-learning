def html_tag(tag):
    def tag_message(message):
        return("<" + tag + ">" + message + "</" + tag + ">")
    return tag_message


p_tag = html_tag("p")
print(p_tag("Hello"))
h1_tag = html_tag("h1")
print(h1_tag("Hello"))
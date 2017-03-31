def insert_tag(text, tag):
    return ("<" + tag + ">" + text + "</" + tag + ">")

print(insert_tag("Dawid", "b"))
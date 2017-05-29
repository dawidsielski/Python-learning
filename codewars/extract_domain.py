"""
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:
"""




def domain_name(url):
    import re
    print(re.search(r"//[www.]?(.*).com", url).group(1))
    return re.search(r"//[www.]?(.*).com", url).group(1)




print(domain_name("http://github.com/carbonfive/raygun") == "github")
print(domain_name("http://www.zombie-bites.com") == "zombie-bites")
print(domain_name("https://www.cnet.com") == "cnet")
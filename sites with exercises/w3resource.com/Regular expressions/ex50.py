import re

sample_data = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]

def extract_domain(url):
    for element in url:
        print(re.sub(r'\s\(.+\)', "", element))


extract_domain(sample_data)
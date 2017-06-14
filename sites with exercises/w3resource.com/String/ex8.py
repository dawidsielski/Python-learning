text = "abracadabra my name is Dawid Sielski".split()

print(text)

text = sorted(text, key = len)
print(len(text[len(text) - 1]))
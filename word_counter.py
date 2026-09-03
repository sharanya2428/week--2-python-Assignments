with open("sample.txt", "r") as f:
    text = f.read()

words = text.split()
lines = text.splitlines()
characters = len(text)

print("Words:", len(words))
print("Lines:", len(lines))
print("Characters:", characters)

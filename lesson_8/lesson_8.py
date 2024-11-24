with open("original.txt", "w") as file:
    file.write("Жизнь — это то, что с тобой происходит, пока ты строишь планы.")

with open("original.txt", "r") as file:
    content = file.read()

with open("reversed.txt", "w") as reversed_file:
    reversed_file.write(content[::-1])

with open("reversed.txt", "r") as reversed_file:
    content2 = reversed_file.read()

print(content)

print(content2)

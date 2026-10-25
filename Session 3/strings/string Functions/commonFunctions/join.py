str = 'A quicck brown fox jumps over the little lazy dog'

print("After using split")
listOfStringWord = str.split()
print(listOfStringWord)

listOfStringWord2 = str.split('a')
print(listOfStringWord2)

print("Before join")
print(listOfStringWord)
print(listOfStringWord2)


print("After using join")
print(" ".join(listOfStringWord))
print(f""" " ".join(listOfStringWord) : {" ".join(listOfStringWord)}""")
print(f""" "@".join(listOfStringWord) : {"@".join(listOfStringWord)}""")



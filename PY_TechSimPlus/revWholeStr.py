# name = "My name is abhishek"
name = input("Enter the string ")
print(name)

nameList = name.split(" ")
print(nameList)

nameList.reverse()
    # print(nameList[::-1])

print(nameList)

ss = " ".join(nameList)
print(ss)


l = name.__len__()

print(l)

line = input("Enter lotto data: ")
list = line.split(",")
listString = list[0:5]
listInt = [int(n) for n in listString]
listInt.sort(reverse=True)
print(listInt)


 
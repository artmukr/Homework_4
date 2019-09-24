test = "test1, test2, test3, test4, test5"
index = int(input("Enter the number :"))
test = test.split()
del test[index]
print(test)


import  random

for i in range(1,20,2):
    print(i)
    a = random.randint(1,100)
    print(str(a%10) + "\n")


list_set = {1,2,3}

print(type(list_set))
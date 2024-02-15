mylist = [0,0,0,0,0,0,0,0,9]
length = len (mylist)

for index, value in enumerate (mylist):
    if value == 0:
        j = index + 1
        while  j < length:
            if mylist[j] != 0:
                mylist[index], mylist[j] = mylist[j], mylist[index]
                break
            j = j+1

print(mylist)
        



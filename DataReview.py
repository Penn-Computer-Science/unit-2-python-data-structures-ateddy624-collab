practice_list=[1,154,235,31,6,32,23,893,94,10]
print("The first number is "+str(practice_list[0]))
print("The last number is "+str(practice_list[9]))
print("The middle number is "+str(practice_list[5]))
practice_list.append(846)
practice_list[2]=99
print("The even numbers are: ")
for i in practice_list:
    if i%2==0:
        print(i)
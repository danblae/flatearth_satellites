f=open("C:\\Users\\7Administrator\\Desktop\\rad\\podacinotpad.txt", "r")
#print(f.read())


sateliti14=open("C:\\Users\\7Administrator\\Desktop\\rad\\sateliti14.txt", "w")
counter14=0

for line in f:
    a=line.split()
    if len(a)==11:
        if float(a[2])>=-14 and float(a[2])<=14:
            counter14 += 1
            sateliti14.write(line)
            #print line


#print counter14
sateliti14.close()

sateliti14=open("C:\\Users\\7Administrator\\Desktop\\rad\\sateliti14.txt", "r")


list=[]
#for line in sateliti14:
#    list.append(sateliti14.readline())
list = sateliti14.readlines()
i = 1
count = 0
print(list.count)
for x in list:
    if float(list[i-1].split()[3]) < 180 and float(list[i].split()[3]) > 180:
        if 180-float(list[i-1].split()[3]) < float(list[i].split()[3]) - 180:
            print(list[i-1])
            count += 1
        else:
            print(list[i])
            count += 1
    elif float(list[i-1].split()[3]) > 300 and float(list[i].split()[3]) < 300:
        if 360-float(list[i-1].split()[3]) < float(list[i].split()[3]):
             print(list[i-1])
             count += 1
        else:
            print(list[1])
            count += 1
    i+=1
    
        

# f.seek(0)

# counter2=0
# sateliti2=open("C:\\Users\\7Administrator\\Desktop\\rad\\sateliti2.txt", "w")

# for line in f:
#     b=line.split()
#     if len(b)==11:
#         if float(b[2])>=-2 and float(b[2])<=2:
#             counter2 += 1
#             sateliti2.write(line)
#             ##print line

# print counter2
# sateliti2.close()



for i in range(11):
    print(i)
    i+=1



for i in range(21):
    if i%2==0:
        print(i)
    else:
        print("")
    i+=2

i=10
while i !=0:
    print(i)
    i=i-1


print("მე დავწერე დავალება, მაგრამ მან არ იმოქმედა და რომ არ გაეფუჭებინა მთელი კოდი, მე იგი არ დავტოვე(წავშალე)")



usernum = int(input("რამდენი ქულა მიიღე?"))
if usernum<60:
    print("F")
elif usernum<70:
    print("D")
elif usernum<80:
    print("C")
elif usernum<90:
    print("B")
elif usernum<=100:
    print("A")





x=int(input('''Enter your choice
                1.Prime No.
                2.Range Prime Number
                3.Leap Year
                4.Range Leap Year
                5.Factor
                6.Factorial
                7.Perfect No.
                8.Palindromic No.
                9.Armstrong No.
                10.Range Armstrong No.
:-  '''))

if x==1:
    i=int(input('Enter the value :-  '))
    x=0
    for y in range(2,i):
        if i%y==0:
            x=1
            break
    if x==0:
            print('Not Prime')
    else:
        print('Prime')


elif x==2:
    i=int(input('Enter 1st value :-  '))
    j=int(input('Enter 2nd value :-  '))
    x=0
    for y in range(i,j+1):
        for i in range(2,y):
            if y%i ==0 :
                break
        else:
            print(y)


elif x==3:
    i=int(input('Enter any Year :-  '))
    x=1
    if i%4==0:
        x+=1
        print('Leap Year')
    else:
        print('Not a Leap Year')


elif x==4:
    i=int(input('Enter Starting Year :-  '))
    j=int(input('Enter End Year :-  '))

    for y in range(i,j+1):
        if y%4== 0:
            if y%100==0:
                if y%400==0:
                    print(y, "Leap Year")
                else:
                    print(y, "Normal Year")
            else:
                print(y, "Leap Year")
        else:
            print(y, "Normal Year")




elif x==5:
    x=int(input("Enter The Number :-  "))
    i=1
    while i<x:
        if x%i==0:
            print(i)
        i=i+1


elif x==6:
    x=int(input('Enter any value :- '))
    i=1
    temp=1
    while i<=x:
        temp+=i
        i+=1
    print('Factorial is :- ',temp)


elif x==7:
    x=int(input("Enter the value  :-  "))
    i=1
    while i<x:
        if x%i==0:
            t=i
            t=t+i
        i=i+1
    if t==x:
        print(i,"is a Perfect No.")
    else:
        print(i,"is not a Perfect No.")


elif x==8:
    i=int(input('Enter any number :-     '))
    temp=i
    s=0
    while temp>0:
        digit=temp%10
        s=s*10+digit
        temp=temp//10
    if s==i:
        print('Its a Palindromic no.')
    else:
        print('Its not a Palindromic no.')


elif x==9:
    i=int(input('Enter any number :-    '))
    temp=i
    s=0
    ln=len(str(i))
    while temp>0:
        digit=temp%10
        s=s+(digit**ln)
        temp=temp//10
    if s==i:
        print('Its a Armstrong no.')
    else:
        print('Its not a Armstrong No.')



elif x==10:
    i=int(input('Enter 1st value :-  '))
    j=int(input('Enter 2nd value :-  '))
    for y in range(i,j+1):
        temp=y
        s=0
        ln=len(str(y))
        while temp>0:
            digit=temp%10
            s=s+(digit**ln)
            temp=temp//10
        if s==y:
            print(y, 'Armstrong no.')
        else:
            print(y, 'is not an Armstrong No.')


else:
    print('Enter Valid Operation')
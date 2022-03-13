car=23*[' ']
s,c=0,0
def move(i,g,s,c):
    car[i-1]=g
    print('    _|___|___|___|_       |       _|___|___|___|_         ')
    print('     | '+car[0]+' | '+car[1]+' | '+car[2]+' |        |       _| 1 | 2 | 3 |_  '+A1 +' :\t',s)
    print('    _|___|___|___|_       |       _|___|___|___|_         ')
    print('     | '+car[3]+' | '+car[4]+' | '+car[5]+' |        |       _| 4 | 5 | 6 |_  '+A2 +' :\t',c)
    print('    _|___|___|___|_       |       _|___|___|___|_         ')
    print('     | '+car[6]+' | '+car[7]+' | '+car[8]+' |        |       _| 7 | 8 | 9 |_')
    print('    _|___|___|___|_       |       _|___|___|___|_         ')
    print("____________________________________________________________")
    return
print("  {welcome to the game [X,O] }")
print("  that is the roles you should chose one the nomber between {1...9}")
print('                     _|___|___|___|_         ')
print('                     _| 1 | 2 | 3 |_         ')
print('                     _|___|___|___|_         ')
print('                     _| 4 | 5 | 6 |_         ')
print('                     _|___|___|___|_         ')
print('                     _| 7 | 8 | 9 |_         ')
print('                     _|___|___|___|_         ')
print("  shel we start who will begin first you or your friend !  ")
A1=str(input("  what is your name to make the game more fany :\t"))
A2=str(input("  what is the name of your friend :\t"))
p1=str(input("      chose {X} or {O}  :\t "))
while p1!='X'and p1!='x' and p1!='o' and p1!='O' :
    print("      please chose {X} or {O}",A1,"  :")
    p1=str(input())
P='yes'
while P!='no' and P!='NO' :
    car=23*[' ']
    if s<=c:
        h,i=10,10
        while h!=1 and h!=2 and h!=6:
            h=h-1
            print(" what is your next move ",A1,"  :(1...9)")
            i=int(input())
            if p1=='O'or p1=='o':
                g='O'
            if p1=='X'or p1=='x':
                g='X'
            while car[i-1]=='O' or car[i-1]=='X'or i<=0 or i>=10: 
                i=int(input(" this nomber is not valable chose one:(1...9)\t")) 
            move(i,g,s,c)
            for i in range(0,7,3):
                if car[i]==g and car[i+1]==g and car[i+2]==g:
                    h=1
            for i in range(0,3,1):
                if car[i]==g and car[i+3]==g and car[i+6]==g:
                    h=1    
            for i in range(0,7,6):
                if car[i]==g and car[4]==g and car[8-i]==g:
                    h=1
            if h!=1:
                print(" what is your next move ",A2,"  :(1...9)")
                i=int(input())
                if p1=='X' or p1=='x':
                    p2='O'
                else:
                    p2='X'
                g=str(p2)
                while car[i-1]=='X' or car[i-1]=='O' or i<=0 or i>=10:
                    i=int(input("tnis nomber is not valable chose an ather one:(1...9)\t"))
                move(i,g,s,c)
                for i in range(0,7,3):
                    if car[i]==g and car[i+1]==g and car[i+2]==g:
                        h=2
                for i in range(0,3,1):
                    if car[i]==g and car[i+3]==g and car[i+6]==g:
                        h=2    
                for i in range(0,7,6):
                    if car[i]==g and car[4]==g and car[8-i]==g:
                        h=2
        if h==1:
            print(" the winer is {",A1,"}")
            s=s+1
        elif h==2:
            print(" the winer is {",A2,"}")
            c=c+1
        else:
            print("the game is tie no one win")
    else:
        h,i=10,10
        print("now you will start ",A2)
        while h!=1 and h!=2 and h!=6:
            h=h-1
            print(" what is your next move ",A2,"  :(1...9)")
            i=int(input())
            g=str(p2)
            while car[i-1]=='O' or car[i-1]=='X'or i<=0 or i>=10: 
                i=int(input(" this nomber is not valable chose one:(1...9)\t")) 
            move(i,g,s,c)
            for i in range(0,7,3):
                if car[i]==g and car[i+1]==g and car[i+2]==g:
                    h=1
            for i in range(0,3,1):
                if car[i]==g and car[i+3]==g and car[i+6]==g:
                    h=1    
            for i in range(0,7,6):
                if car[i]==g and car[4]==g and car[8-i]==g:
                    h=1
            if h!=1:
                print(" what is your next move ",A1,"  :(1...9)")
                i=int(input())
                g=str(p1)
                while car[i-1]=='X' or car[i-1]=='O' or i<=0 or i>=10:
                    i=int(input("tnis nomber is not valable chose an ather one:(1...9)\t"))
                move(i,g,s,c)
                for i in range(0,7,3):
                    if car[i]==g and car[i+1]==g and car[i+2]==g:
                        h=2
                for i in range(0,3,1):
                    if car[i]==g and car[i+3]==g and car[i+6]==g:
                        h=2    
                for i in range(0,7,6):
                    if car[i]==g and car[4]==g and car[8-i]==g:
                        h=2
        if h==2:
            print(" the winer is {",A1,"}")
            s=s+1
        elif h==1:
            print(" the winer is {",A2,"}")
            c=c+1
        else:
            print("the game is a tie no one win ")
    P=str(input("do you want to play again (yes,no)"))

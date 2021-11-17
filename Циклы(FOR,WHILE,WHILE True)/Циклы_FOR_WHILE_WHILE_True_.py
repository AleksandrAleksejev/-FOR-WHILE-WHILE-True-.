





#28
#from random import *
#print("Loterii".center(50,"*"))
#A=randint(1,5)
#B=int(input("Введи загаданное число ->"))
#if A==B:
#    print("Молодец ты выйграл!!!!!")
#else:
#    print("К сожалению, вы проиграли:(,попробуй еще ")

    


#Купи слона 
#loom=input('Купи слона!')
#while loom.title()!="Слон":#upper(),lower()
#    loom=input('Все говорят '+loom+"! А ты купи!!!")
#print('Молодец!!!')





#29
#for rjady in range(1,10):
#    for stroka in range(1,10):
#        if rjady==stroka:
#            print("x",end=" ")
#        elif stroka==1:
#            print("x",end=" ")
#        else:
#            print('0',end=' ')
#    print()



#16
#for rjady in range(1,10):
#    for stroka in range(1,10):
#        if rjady==stroka:
#            print(stroka,end=" ")
#        else:
#            print('0',end=' ')
#    print()



##15
#for rjady in range(10):
#    for stroka in range(10):
#        print(stroka,end=' ')
#    print()

##13
#k=0
#summa=0
#for i in range (100,1001):
#    if i % 7==0:
#        print(i)# viveli na ekraan
#        k+=1 #zislo
#        summa+=i # i-de summa,kotorie deljatsja na 7 
#print("kogus: ",k)
#print("Summa: ",summa)





##9
#p=1.03
#S=int(input("Sissesta summa ->"))
#N=int(input("Mitu aastat ->"))
#for aasta in range(1,N+1):
#    S*=p
#    print(aasta,"aasta parast tulemus on",round(S,2))





#2zadatsja
#A=input("Sissesta Arv")
#while int(A)<=1:
#    try:
#        A=int(input("Sissesta "+str(i+1)+" Arv"))
#    except:
#        TypeError
#Summa=0
#for i in range(1,int(A)+1):
#    Summa+=1
#print("Summa vordub",Summa)






#3zadatsja 
#korrutis=1
#for i in range (8):
#    arv=float(input(f"{i+1} Arv:"))
#    if arv>0:
#        korrutis*=arv
#print(korrutis)

        
#    while type (A)!=float:
#        try:
#            A=float(input(f"Sisesta {i+1} arv ->"))
#        except ValueError:
#            print("Oi")
#Z=float(input(A*A))

#8zadatsja
#for i in range (1,21):
#    print("duim ="+ str(i*2.5),"Cm")

#zadatsja 6
#from random import *
#p=0
#n=0
#N=randint(1,10)
#print(N)
#for i in range(N):
#    Arv=int(input("Sissesta arv"))
#    if Arv>0:
#        p+=1
#    elif Arv<0:
#        n+=1
#print("Neg"+str(n))
#print("Pos"+str(p))
#print("Nullid"+str(N-n-p))





#from random import * #7 
#A<B
#A=randint(10,100)#рандомное число от 10 до 100
#B=randint(100,1000) 
#K=int(input("K:"))
#for i in range(A,B+1):
#    if i%K==0: print(i)





#for x in range (10): #0....9
 #   print ("Hello World")
#for x in range (1,11):#1..10
#    print ("Hello World")      
#for x in range (start,stop,step):#0...N-1
 #   print ("Hello World")  
#p=0 #1 zadatsja
#for i in range (15): #i=0,1,2,3... #выводится от 1 до 15 чисел 
#    A=0
#    while type (A)!=float:
#        try:
#            A=float(input(f"Sisesta{i+1}arv ->"))
#        except ValueError:
#            print("Oi") #пишнт при ошибке коммент
#    if A==round(A): #округление
#       p+=1
#        print(str(A)+"on taisarv")
#    else:
#        print(str(A)+"ei ole taisarv")

#print(str(p)+"Taisarvud") #выводит сколько чисел получилось #4zadatsa
#for i in range(10,21):
#    print(i**2)

from random import *
from math import *
#from keyboard import *

print("Контроль знаний".center(60,"*"))
tase=int(input("Выбери сложность 1 (Легкий), 2 (Средний), 3 (Сложный): "))
tase=0
while tase not in [1,2,3]:
    try:
        tase=int(input("Выбери сложность 1 (Легкий), 2 (Средний), 3 (Сложный): "))
    except ValueError:
        print("Ainult 1,2 või 3!")
    except:
        print("Ainult 1,2 või 3!")
if tase==1:
    min=2
    max=10
    tehed=["+","-"]
elif tase==2:
    min=2
    max=15
    tehed=["+","-","*"]
elif tase==3:
    min=2
    max=20
    tehed=["+","-","*","//"]
else:
    min=2
    max=20
    tehed=["+","-","*","//"]

p=0
kokku=0
while True:
       v=input("Kas jatkame? enter=jah, stop=ei")
       if v=='stop':
           break
       else:
           kokku+=1
           a=randint(min,max)# !=0
           b=randint(min,max)# !=0
           tehe=choice(tehed)#
           if tehe=="//":
               while b==0:
                   try:
                       b=randint(min,max)
                   except:
                        ValueError
           print(f"{a}{tehe}{b}", end=" ")
           vaja=int(eval(str(a)+tehe+str(b))) #round()?
           vastus=""
           while type(vastus)!=int:
               try:
                  vastus=int(input("=")) #!=str
               except ValueError:
                  print("vaja int!!!")
           if vastus==int(vaja):
             print("Правильный ответ!")
           else:
             print("Не правильный ответ!")

print("Kokku ulesandeid oli: ",kokku)
print("Правильных ответов: ",p)
K=(p/kokku)*100
if K<60:
    print("Hinne 2")
elif 60<=K<75:
    print("Hinne 3")
elif 75<=K<90:
    print("Hinne 4")
elif K>90:
    print("Hinne 5")



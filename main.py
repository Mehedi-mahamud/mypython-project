
marks =int(input("inter your mark:"))
if marks >= 80 :
    print("GPA is A+")
elif marks >= 70:
    print("GPA is A")
elif marks >= 60:
    print("GPA is A-")
elif marks >= 50:
    print("GPA is B")
else:
    print("End")


x=int(input("Inter a number:"))
if x>=0:
    if x % 2 ==0:
         print("number is positive and even")
    else:
        print("number is positive and odd")
else:
    if x % 2 ==0:
         print("number is nagative and even")
    else:
        print("number is nagative and odd")
   


x =int(input("inter a number :"))

if x>=0 and x % 2==0:
    print("Its a positive and even number")
elif x>=0 and x%2==1:
    print("Its a positive and odd number ")
elif x<0 and x%2==0:
    print("Its a nagative and even number")
else:
    print("Its a nagative and odd number")




if x % 2 == 0:
    print(x,"is even")
else:
    print(x,"is odd")


year =int(input("Inter a year:"))

if year % 400 ==0:
    print(year,"is leap year")
elif year % 4 == 0 and year % 100 !=0:
    print(year,"leap year")
else:
    print(year,"is not leap year")


day = input("whitch day today:")
day = day.lower()
sick = input("are you sick today:")
sick = sick.lower()
if day == ("friday" or "satuerday") and sick == "no":
    print("I have to go school today")
else:
    print("i don't have to go school")


n = int(input().strip())
if n % 2 !=0:
    print("Weird")
elif n % 2 ==0 and 2<n<5:
     print("Not Weird")
elif n % 2 ==0 and 6<n<20:
    print("Not Weird")
elif n % 2==0 and n>20:
        print("Not Weird")
else:
    print("Weird")


words ={
    "home":"bari",
    "help":"sahajjo",
    "cat" :"biral"
}
word = input("Enter a word:")

print(words[word])



a1 =int(input("inter a mark 1:"))
a2 =int(input("inter a mark 2:"))
a3 =int(input("inter a mark 3:"))

total_prcentange = (a1 + a2 + a3)/3

if (total_prcentange>40 and a1>=33 and a2>=33 and a3>=33):
    print("You are pass",total_prcentange)
else:
    print("You faild",total_prcentange)



n = int(input())
i= 1
while i <= 10:
    print(n,"x =",n*i) 
    i +=1


num=(2, 4 ,5 ,6 , 7 , 8 ,9 ,10)

x=int(input())
i=0
while i<len(num):
    if(num[i])==x:
        print("found in index",i)
        break
    else:
        print("finding....")
    i +=1

num=[1, 2, 4, 8, 4]
idx = 0
for i in num:
    if (i==4): 
       print("number found in index", idx)
    idx +=1  



def table_01(a,b):
    sum = a + b
    sub = a - b 
    mul = a * b
    print(sum, sub , mul)

table_01(4,5)
x = 3



import os 

mylist = ['apple', 'banana', 'cherry']
mylist.insert(0, 'orange')
print(mylist)

fruits = ['apple', 'banana', 'cherry']
newlist = [x for x in fruits if x == 'banana']
print(newlist)


# greter number find 
a =int(input())
b =int(input())
c =int(input())
def find_number_greter(a, b, c):
    if a > b and a > c :
        print(f"{a} is the greater number")
    elif b > a and b > c :
        print(f"{b} is the greater number")
    else:
        print(f"{c} is the greter number")

find_number_greter(a, b, c)


#
def is_leap(year):
    # Check if the year is divisible by 400 (leap yea0:
    if year % 400 == 0:
        return True
    # Check if the year is divisible by 100 but not by 400 (not a leap yea0:
    if year % 100 == 0:
        return False
    # Check if the year is divisible by 4 (leap yea0:
    if year % 4 == 0:
        return True
    # Otherwise, it's not a leap ye0:
    return False

year = int(input())
print(is_leap(year))



def multiplecation_table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {i*n}")

n=int(input())
multiplecation_table(n)


dict_01 = {1: "mehedi", 2:"dipto"}
print(dict_01[1])

import os 
# os.rmdir("new")

import shutil

shutil.make_archive("game", "zip", "new")

with open("opp.py","w") as f:
    f.write()

import random

def game():
    score=random.randint(1,50)
    with open ("hiscore") as f:
        hiscore=f.read()
        if hiscore!="":
            hiscore = int(hiscore)
        else:
            hiscore=0
    print(f"your score is {score}")
    if (score > hiscore or hiscore ==""):
        with open ("hiscore","w") as f:
            f.write(str(score))
    return score

game()



print("hello world")
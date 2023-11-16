import random
import time
import matplotlib.pyplot as pyp
time.sleep(1)
print("Welcome to the typing speed calculator, here there will be 5 rounds where you will write a particular word and we will find how fast is your typing!, Good luck!")
list_of_words=["blue","yellow","hello","good","green","thanks","red","akul"]
word=list_of_words[random.randint(0,7)]
print("You have to write the word:",word)
print("Your round starts in 10 seconds")
for i in range(10,-1,-1):
    print(i)
    if(i!=0):
        time.sleep(1)
y=[]
error=0
for i in range(0,5):
    t1=time.time()
    n=input("Enter word:")
    t2=time.time()
    t=t2-t1
    y.append(t)
    if(n!=word):
        error +=1
x=[1,2,3,4,5]
print("----------------------")
print("The word was:",word)
print("The numbers of errors made:",error)
if(error==0):
    print("Well done!, no mistakes made!")
sum1=0
for i in (y):
    sum1 = sum1 + i
avg=sum1/5
print("Your average time is:",round(avg,2)," seconds")
pyp.bar(x,y)
pyp.title("Typing speed chart")
pyp.ylabel("Time taken in seconds")
pyp.xlabel("Rounds")
time.sleep(5)
pyp.show()

#exercise 1
list1=[54,76,2,4,98,100]
int1=int(input("please enter first number: "))
int2=int(input("please enter second number: "))

for i in list1:
  if int1>int2:
    print("first number cant be bigger than the second number")
    break
  elif i>=int1 and i<=int2:
    print(i)


#exercise 2
names=["maria","Hala","Ghady","Ehsan","Joe","Zoe"]
letter=input("please enter a letter: ")
for i in range(len(names)):
  if letter in names[i].lower():
    print(names[i])

# #exercise 3
numbers=[-12, 4, 12, 25, 67]
userNumber=int(input("please enter a number: "))

while userNumber !=-99:
  index=0
  for i in range(len(numbers)):
    if numbers[-1]<userNumber:
      index=len(numbers)
      break
    elif numbers[i]>userNumber:
      index=i
      break
  
  numbers.insert(index,userNumber)
  print(numbers)
  userNumber=int(input("please enter a number: "))

#exercise 4
words="Is this the real life? Is this just fantasy? Caught in a landslide,no escape from reality Open your eyes, look up to the skies and see I\'m justa poor boy, I need no sympathy Because I\'m easy come, easy go, little high,little low Any way the wind blows doesn\'t really matter to me, to me Mama,just killed a man Put a gun against his head, pulled my trigger, now he\'s dead Mama, life had just begun But now I\'ve gone and thrown it all away Mama,ooh, didn\'t mean to make you cry If I\'m not back again this time tomorrow Carry on, carry on as if nothing really matters Too late, my time has comeSends shivers down my spine, body\'s aching all the time Goodbye, everybody,I\'ve got to go Gotta leave you all behind and face the truth Mama, ooh (anyway the wind blows) I don\'t wanna die I sometimes wish I\'d never been born at all I see a little silhouetto of a man Scaramouche, Scaramouche, will you do the Fandango? Thunderbolt and lightning, very, very frightening me (Galileo)Galileo, (Galileo) Galileo, Galileo Figaro, magnifico But I\'m just a poor boy, nobody loves me He\'s just a poor boy from a poor family Spare him his life from this monstrosity."

int1=int(input("please enter a start point: "))
int2=int(input("please enter an end point: "))

letterList=[]

for letter in words:
  letterList.append(letter)

for i in range(len(letterList)):
  if int1>int2:
    print("starting point cant be bigger than the ending point")
    break
  elif i>=int1 and i<=int2:
    print(letterList[i],end='')
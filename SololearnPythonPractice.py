#Practice Project № 1
print(((1*2)**30)/100)

#Practice project № 2 
first=int(input())
second=int(input())
print(first+second)

#Practice project № 3
n = int(input())

for x in range(1, n):
    if x % 3 == 0 and x % 5 == 0:
        print("SoloLearn")
    elif x % 3 == 0:
        print("Solo")
    elif x % 5 == 0:
        print("Learn")
    else:
        print(x)

#Practice project № 4
celsius = int(input())

def conv(c):
    return 9/5*c+32

fahrenheit = conv(celsius)
print(fahrenheit)

#Practice project № 5
file = open("/usercode/files/books.txt", "r")

for line in file:
      if line[-1] == "\n":
          print(line[0]+str(len(line)-1))
      else:
             print(line[0]+str(len(line)))


file.close()

#Practice project № 6
txt = input()
point = 0
txtList=txt.split(" ")
word=""
for i in txtList:
    if len(i)>len(word):
        word=i
print(word)

#Practice project № 7
num = int(input())
def fibonacci(n):
    if n <= 1:
        return n

    else:
        return fibonacci(n-1) + fibonacci(n-2)


for number in range(num):
    print(fibonacci(number))

#Practice project № 8
class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return (self.name + ' (' + str(self.capacity) + 'L)')

    def __add__(self, newJuice):
        self.name += "&" + str(newJuice.name)
        self.capacity += newJuice.capacity
        return self.__str__


a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)

print(a.__add__(b)())

#Practice project № 9
import re

if re.match('^[189][0-9]{7}$',input()):
    print("Valid")
else:
    print("Invalid")

#Practice project №10
def concatenate(first,*args):
    text=first+"-"
    for i in args:
        text+=i+"-"

    return text[:-1]

print(concatenate("I", "love", "Python", "!"))
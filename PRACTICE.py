print("Hello World")
print("   /|")
print("  / |")
print(" /  |")
print("/___|")
character_name = "Temiloluwa"
important_date = "20th of august"
print("I met a man named "  + character_name + ",")
print("He turned my world upside down")
print ("On the "  + important_date)
print(character_name +  " was a sight for sore eyes")
print("and on the "  + important_date + " he smiled at me")
phrase = "I love milkshakes"
print(phrase)
print(phrase.lower())
print(phrase.lower().isupper())
print(len(phrase))
print(phrase.replace("milkshakes","Temi"))
print(phrase[0])
print(phrase[2])
first = "Data makes work easier, "
second = " while science combines"
print(first + second)
age = 25
print("i am " + str(age) )
print("I went to the market", end= " ")
print("and bought chicken")
print(344 * 344)
print(5673 + 8675)
print("I am",35,"years old.")
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")
print(type(age))
print(type(first))
myvar = "John "
my_var = "loves "
_my_var = "his "
myVar = "ice-cream "
MYVAR = "very "
myvar2 = "creamy"
print(myvar + my_var  + _my_var  + myVar  + MYVAR  + myvar2)
fruits = ["apple", "banana", "cherry", "Kiwi"]
x, y, z, p = fruits
print(x)
print(y)
print(z)
print(p)
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)
x = range (9)
print(x)
print(list(x))
x = frozenset ({"apple", "banana", "cherry"})
print(x)

x = 1
y = 2.8
z = 1j
a = float(x)
b = int(y)
c = complex(x)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

for x in "banana":
  print(x)
txt = "The best things in life are free!"
print("free" in txt)
reg = "love yourself today"
print("your" in reg)
print("y" in reg)
print("three" in reg)

if "free" in txt:
  print("Yes, 'free' is present.")
txt = "The best things in life are free!"
print("expensive" not in txt)
print("expensive" in txt)
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
if "best" not in txt:
  print("No, 'best' is NOT present.")
else: print("Yes")
b = "Hello, World!"
print(b[0:5])
print(b[7:12])
print(b[0:1])
print(b[0])
print(b[7])
print(b[-1])
print(b[-1])
print(b[-2])
print(b[-6:-1])
sentence = "I want to be an AI Engineer"
print(sentence.replace("AI Engineer", "Python Developer"))
print(sentence.split())
print(sentence.split(","))
print(sentence.split("be"))
print(sentence.split("Engineer"))
age = 36
txts = "My name is John, I am " + str(age)
print(txts)
age = 34
txt = f"My name is John, I am {age} years old."
print(txt)
price = 59.9999
print(f"The price is {price:.2f} dollars")
print(f"The price is {price:.2} dollars")
print(f"The price is {price:.3f} dollars")
price = 100
print(f"The price is {price:.2f} dollars")
price = 3.14159
print(f"The price is {price:.4f} dollars")
print(f"The price is {price:.4} dollars")
price = 59
txt = "The price is {price:.2f} dollars"
print(txt)
name = ""
if name:
    print("Name exists")
else:
    print("Name is empty")
print(bool(""))
print(bool(0))
print(bool("0"))
print(bool(-5))
def has_credit():
    return False
if has_credit():
    print("Call the API")
else:
    print("Top up your account first")
def myFunction():
    pass
print(myFunction())

x = 15
y = 4

print(x % y)
print(x // y)
print(x == 15 and y > 5)
print(x == 15 or y > 5)
x += 5
print(x)

a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("no")
if a + b == 233:
    print("yes")
else:
    print("no")

age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)
age_2 = 15
status = "Adult" if age_2 >= 18 else "Minor"
print(status)

x = 5
y = 3
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

x = 5
print(1 < x < 10)
print(1 < x and x < 10)

x_o = 5
print(not(x_o > 10))
print(not(x_o == 5))
print(not(x_o > 3 or x > 10))

thislist = ["apple", "banana", "cherry"]
print(thislist)
my_set = {"apple", "banana", "cherry"}
my_list = list(my_set)
print(my_list)

thislist = list(("apple", "banana", "cherry"))
print(thislist)

this_list = ["a", "b", "c"]
t_l = list(this_list)
print(t_l)

this_list = ["a", "b", "c"]
thislist = list(thislist)
print(thislist)

mylist = ["apple", "banana", "cherry"]
mylist[0:2] = ("mango", "kiwi")
print(mylist)

myset = {"apple", "banana", "cherry"}

myset.add("mango")
myset.discard("apple")
print(myset)

mybrands = ["Cocacola", "Gwagon", "Cheese"]
for brand in mybrands:
    print("I love " + brand)

mylist = ["Comfort", "Lagos", "Python", "AI Engineer"]

for x in range(len(mylist)):
    print(x, mylist[x])


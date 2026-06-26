print("hello world", 7 )
print(5)
print("Bye")
print(17*12)
print("hey i am a good girl \n and i am also very intelligent")
# this is a single- line comment
print (" this is a print statement.")
print ("hello world!!!") # printing hello world
print ("hey", 6, 7, sep="-" , end="009 \n ")
print ("harman")
a=1234566778888288
print(a)
b= "kajal"
print(b)
a=1 
print(type(a))
b="1"
print(type(b))
a= complex(6, 2)
print(type(a))
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)
tuple1 = (("parrot", "sparrow"), ("lion", "tiger"))
print(tuple1)
name = "hargun"
friend = "anmol"
anotherfriend = 'arsh'
pie = "applepie"
print(pie[:5])
print(pie[6]) 
pie = "applepie"
print(pie[:5])
print(pie[5:])
print(pie[2:6])
print(pie[-8:])
alphabets = "ABCDE"
for i in alphabets:
    print(i)
nm = "harry" 
print(nm[-4:-2])
a ="kajal"
print(len(a))
print(a.upper())
print(a.lower())
#arithmetic operator
a = 5
b = 6
print(a+b)  #addition 
print(a-b)  #subtraction
print(a*b)  #multiplication
print(a/b)  #division
print(a**b) #exponential
print(a//b) #float division
print(a%b)  #modulus
# assignment operator
x = 5
print(x)     # assignment operator
x+=7
print(x)     #addition and assign
x-=7
print(x)    #subtraction and assign
x*=7
print(x)    #multiplication and assign
x/=7
print(x)    #division and assign
x%=7
print(x)    #modulus and assign
x**7
print(x)    #exponential and assign
#comparison operator
a=8
b=5
print(a==b)  #equal to
print(a>b)   #greater than
print(a<b)   #less than
print(a>=b)  #greater than or equal to
print(a<=b)  #less than or equal to
print(a!=b)  #not equal to
#ogical operator
a = 5
b = 10
print(a>b and b<a) #and
print(a>b or b<a)  #or
print(a<b and b>a) #and
print(a<b or b>a)  #or
print(not(a>b))    #not
print(not(a<b))    #not
#membership operator
numbers = [5, 10, 15, 20]
print(10 in numbers)      #present
print(25 in numbers)      #present
print(25 not in numbers)  #not present
print(10 not in numbers)  #not present
#identity operator
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)      #same object
print(a is c)      #same object
print(a is not c)  #different object
#bitwise operator
a=5
b=3
print(a&b)  #AND
print(a>>b) #right shift
print(a<<b) #left shift
print(a<<b) #left shift
print(~a)  #NOT
print(a^b) #XOR
#strip
str2 = "silver spoon"
print(str2.strip)
#rstip
str3 = "hello !!!"
print(str3. rstrip("!"))
#replace
str2="silver spoon"
print(str2.replace("sp","m"))
#split
str2="silver spoon"
print(str2.split(" "))
#capitalize
str1="hello"
capstr1 = str1.capitalize()
print(capstr1)
str2="hello worlD"
capstr2 = str2.capitalize()
print(capstr2)
#center
str1 = "welcome to the console !!!"
print(str1.center(50))
str1 = "welcome to the console !!!"
print(str1.center(50, "."))
#count
str2 = "kajal"
countstr2 = str2.count("a")
print(countstr2)
age=int(input("enter your age"))
if age>18:
        print("you can apply for license")
        print("speed thrils but kills")


password = input("password daal: preet")
length = len(password)
if length<6:
      print("password strength: weak")
elif length>=6 and length<=10:
     print("password strength: medium")
elif length>10:
      print("password strenghth: strong")
else:
      print("something is wrong")
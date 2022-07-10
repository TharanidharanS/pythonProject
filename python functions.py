#1.	Write a Python function to find the Max of three numbers.
a=10
b=200
c=30
print(min(a,b,c))


def maximum(a, b, c):
 if (a > b) and (a > c):
  max=a
 elif (b > a) and (b > c):
  max=b
 else:
  max=c
 return max
print(maximum(22,15,20))

 #2.	Write a Python function to sum all the numbers in a list.
 #Sample List: (8, 2, 3, 0, 7)
#Expected Output : 20
n=(8,2,3,0,7)
sum=sum(n)
print (sum)

def add(number):
	 sm = 0
	 for x in number:
	       sm += x
	 return sm
print(add((8,2,3,0,5)))

#3.	Write a Python function to multiply all the numbers in a list.
#Sample List: (8, 2, 3, -1, 7)
#Expected Output : -336

def prod(numbers):
	 mi=1
	 for x in numbers:
	    mi *= x
	 return mi
print(prod((8, 2, 3, -1, 7)))

numbers=(8,2,3,-1,7)
prod=prod(numbers)
print(prod)

#4.	Write a Python program to reverse a string.
#Sample String : "1234abcd"
#Expected Output : "dcba4321"
str="tarun"
print(str[::-1])

def reverse(s):
	s = s[::-1]
	return s
s = "Geeksforgeeks"
print(reverse(s))


def reverse(s):
    str = ""
    for i in s:
        str =i +str
    return str
s= "welcome"
print(reverse(s))

#5.	Write a Python function to check whether a number falls in a given range.


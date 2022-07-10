#1.	Write a Python program to sum all the items in a list.
list=[1,2,3,4,5,6,7,8]
total=sum(list)
print(total)

list = [1, 2, 3, 4, 5, 6, 7, 8]
sum = 0
for i in list: sum += i
print(sum)
#2.	Write a Python program to multiply all the items in a list.
list=[1,2,8]
product=1
for i in list: product *=i
print(product)

#3.	Write a Python program to get the largest number from a list
list = [1, 2, 3, 4, 5, 6, 7, 8]
x=max(list)
print(x)

#4.	Write a Python program to get the smallest number from a list
list = [1, 2, 3, 4, 5, 6, 7, 8]
x=min(list)
print(x)

#5.	Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
list1=['red','green','white','black','pink','yellow']
list1.remove('red')
print(list1)

list1=['red','green','white','black','pink','yellow']
result=[x for i,x in enumerate(list1) if i not in (0,4,5)]
print(result)

#6.	Write a Python program to append a list to the second list
list = [1, 2, 3, 4, 5, 6, 7, 8]
list1=['red','green','white','black','pink','yellow']
result=list+list1
print(result)

list = [1, 2, 3, 4, 5, 6, 7, 8]
list1=['red','green','white','black','pink','yellow']
list.append(list1)
print(list)

list = [1, 2, 3, 4, 5, 6, 7, 8]
list1=['red','green','white','black','pink','yellow']
list.extend(list1)
print(list)

#7.	Write a Python program to count the number of elements in a list within a specified range.
list = [1, 2, 3, 4, 5, 6, 7, 8]
count=0
for index in range (len(list)):count+=1
print(count)
#8.	Write a Python program to calculate the length of a string.
list = ['covai']
print(len(list))
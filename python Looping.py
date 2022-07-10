#while loop
i=1
while i<6:
    print(i)
    i+=1

#while loop with  if condition using break
i=0
while i<7:
    print(i)
    if i == 4:
       break
    i += 1

#while loop with  if condition using continue
i=0
while i<7:
    i += 1
    if i == 5:
       continue
    print(i)

#for loop
team=["csk","mi","rr","kkr"]
for i in team:
    print (i)

 # for loop using break statement
team = ["csk", "mi", "rr", "kkr"]
for i in team:
    print(i)
    if i=="rr":
     break

#for loop with continue statement
fruits=["apple","banana","cherry","fig"]
for i in fruits:
    print(i)
    if i=="cherry":
        break

#for loop with continue statement
fruits=["apple","banana","cherry","fig"]
for i in fruits:
    if i == "cherry":
      continue
    print(i)



fruits = ["apple", "banana", "cherry", "fig"]
for i in fruits:
  if i == "cherry":
     break
  print(i)




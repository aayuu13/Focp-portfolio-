import random
#Constants
NAME=["eric","ram","alex","max","ray","abhi","sohan","bryan"]
COLOR=["red","blue","orange","green","pink","black","white","purple"]
FOOD=["apple", "banana", "cherry","milk","tea","juice","orange","avocado"]
print("PASSWORD GENERATOR")
print("==================")
print("\n")
#To find the number of unique passwords generated
s = set()
while True:
    try:
        num_of_pw=int(input("How many passwords are needed?:"))
        break
    except: 
        print("Please enter a number.")
if num_of_pw==0:
    print("Please enter a value between 1 and 24.")
elif num_of_pw>=24:
    print("Please enter a value less than 24.") 
    exit()   

for i in range(num_of_pw):   
    first=random.choice(NAME)
    second=random.choice(COLOR)
    third=random.choice(FOOD)
    pwd=(first+second+third)
    s.add(pwd)
    print('{}--->{}'.format(i+1,pwd))
  
# print(len(s))
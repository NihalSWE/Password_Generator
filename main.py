import string
import random

characters=list(string.ascii_letters+string.digits+"!@#$%^&*()")


def generate_password():
    pass_len=int(input("ENter Pass limit: "))
    random.shuffle(characters)
    password=[]
    for i in range (pass_len):
        password.append(random.choice(characters))
    random.shuffle(password)
    password="".join(password)
    print ("Your Password is:",password)

option=input("Do You want to generate Password ? (Yes/No): ")
if option =="Yes":
    generate_password()
    
elif option =="No":
    print("Program Ended")
    exit()
    
else:
    print("Invalid Input, Please Input Yes/No")
    exit()
    
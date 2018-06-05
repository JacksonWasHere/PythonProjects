import random
import json

def myHash(string,base):
    seed = sum(ord(num) for num in string)
    random.seed(seed)
    randnum = random.randint(0,pow(2,base))
    out = ""
    for char in string:
        char = ord(char)
        char = char*randnum
        out += str(char)
    # print(out)
    return out

def enter():
    print("----Log in or Sign up-----")
    print("1: sign up\n2: log in")
    choice = input()
    if choice=="1":
        createMode(False,False)
    elif choice=="2":
        signIn(False)

with open("test.json") as f:
	data=json.load(f)

def createMode(exists,password_no_match):
    if exists:
        print("that name exists")
    elif password_no_match:
        print("passwords don't match")
    else:
        print("-----create account-----")
    name = input("username: ")

    for all_names in data['people']:
        if all_names['name']==name:
            createMode(True,False)
            return

    password = input("password: ")
    password_check = input("retype password: ")

    if not password==password_check:
        createMode(False,True)
        return
    data['people'].append({
        "name":name,
        "password":myHash(password,16)
    })

def signIn(wrong):
    if wrong:
        print("-----Wrong name/password-----")
    else:
        print("-----Sign in-----")
    username = input("username: ")
    password = input("password: ")

    for all_names in data['people']:
        if all_names['name']==username:
            if all_names['password']==myHash(password,16):
                print("your in")
                return
    signIn(True)
enter()
with open('test.json', 'w') as outfile:
    json.dump(data, outfile)

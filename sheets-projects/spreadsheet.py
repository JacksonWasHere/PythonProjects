from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import json
from json_manipulation import data_storage

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)
client = gspread.authorize(creds)
person_sheet = client.open('python-datastore').sheet1
message_sheet = client.open('python-datastore').worksheet("Sheet2")

pp = pprint.PrettyPrinter()

personalLogin=data_storage("messengers.json")
global current_user
current_user="guest"

class comment(object):
    """docstring for comment."""
    def __init__(self, words, date, sender):
        super(comment, self).__init__()
        self.date = date
        self.months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
        self.sender = sender
        self.words = words
    def getDate(self):
        cur=self.date
        return str(self.months[cur.month])+" "+str(cur.day)+", "+str(cur.year)+". "+str(cur.hour)+":"+str("cur.minute")+":"+str(cur.second)+"\n"
    def getContent(self):
        return self.words
    def toString(self):
        return self.sender+" said:\n'"+self.words+"'\nat "+self.getDate()

def login():
    print("---------------")
    print("Welcome to our messaging program!")
    print("if you don't have an account please contact the administrator")
    username=input("name: ")
    password=input("password: ")
    if personalLogin.getDataAtPath("users/"+username+"/password/")==password:
        global current_user
        current_user=username
        print("---------------")
        conversations()

def conversations():
    colIndex=0
    print(current_user)
    for i in range(person_sheet.col_count):
        print(person_sheet.cell(1,i+1).value==current_user)
        if person_sheet.cell(1,i+1).value==current_user:
            colIndex=i+1
            break
    messages=""
    for mess in range(person_sheet.row_count):
        value=person_sheet.cell(mess+1,colIndex).value
        if mess==0:
            print("Messages for "+current_user+":\n")
        else:
            messages+=(value if not value=="end" else "")+"\n"
        if value=="end":
            break
    print(messages)
    choice=input("Choose a message: ")
    enter_messages(choice)
    print("---------------")

def showAll(colIndex):
    messages = []
    for mess in range(message_sheet.row_count):
        value = message_sheet.cell(mess+1,colIndex).value
        if mess==0:
            print("Messages in "+message_sheet.cell(1,colIndex).value)
        else:
            messages.append((value if not value=="end" else "")+"\n")
        if value=="end":
            break
    out=""
    for i in reversed(messages):
        out+=i
    return out

def enter_messages(message):
    colIndex=0
    for i in range(message_sheet.col_count):
        if message_sheet.cell(1,i+1).value==message:
            colIndex=i+1
            break
    print(showAll(colIndex))
    talking=True
    while talking:
        send = input("Send: ")
        if send=="-x-":
            talking=False
        else:
            row=[comment(send,datetime.now(),current_user).toString()]
            message_sheet.insert_row(row,2)
        print("----")
        print(showAll(colIndex))
        print("----")
login()

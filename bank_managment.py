import json
import random
import string
from pathlib import Path
class Bank:
    database='data.json'
    data=[]
    try:
        if Path(database).exists():
            with open(database,'r') as fs:
                data=json.loads(fs.read())
        else:
            print('no file can be exist')
    except Exception as err:
        print(f'An exception occured as {err}')
    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))
    @classmethod
    def __accountgenerate(cls):
        alpha=random.choices(string.ascii_letters,k=3)
        num=random.choices(string.digits,k=3)
        sp_char=random.choices("!@#$%^",k=1)
        acc=alpha+num+sp_char
        random.shuffle(acc)
        return "".join(acc)        
    def create_account(self):
        info={
            'name':input('Please enter your name: '),
            'age':int(input('Please enter your age: ')),
            'email':input('Please enter your email: '),
            'pin':int(input('Please enter your 4 number pin: ')),
            'accountno':Bank.__accountgenerate(),
            'balance':0
        }
        if info['age']<18 or len(str(info['pin']))!=4:
            print('Sorry you cannot create account.')
        else:
            print('\nAccount has been created successfully')
            for i in info:
                print(f'{i} : {info[i]}')
            print("Please note your account")
            Bank.data.append(info)   
            Bank.__update()
    def depositmoney(self):
        ac_no=input("Enter your account number: ")
        pin=int(input('Enter your pin: '))
        userdata=[i for i in Bank.data if i ['accountno']==ac_no and i['pin']==pin]
        if userdata==False:
            print('sorry no data found')
        else:
            amount=int(input('Enter amount for deposit: '))
            if amount>10000 or amount<=0:
                print('Please enter valid amount')
            else:
                userdata[0]['balance']+=amount
                Bank.__update()
                print('Deposit succesfully')
    
    def withdraw(self):
        ac_no=input("Enter your account number: ")
        pin=int(input('Enter your pin: '))
        userdata=[i for i in Bank.data if i ['accountno']==ac_no and i['pin']==pin]
        if userdata==False:
            print('sorry no data found')
        else:
            amount=int(input('Enter amount for withdraw: '))
            if userdata[0]['balance']<amount:
                print('Please enter valid amount')
            else:
                userdata[0]['balance']-=amount
                Bank.__update()
                print('Withdraw succesfully')
    def showdetails(self):
        ac_no=input("Enter your account number: ")
        pin=int(input('Enter your pin: ')) 
        userdata=[i for i in Bank.data if i ['accountno']==ac_no and i['pin']==pin]
        for i in userdata[0]:
            print(f'{i}:{userdata[0][i]}')
    def updatedetails(self):
        ac_no=input("Enter your account number: ")
        pin=int(input('Enter your pin: ')) 
        userdata=[i for i in Bank.data if i ['accountno']==ac_no and i['pin']==pin]
        if userdata==False:
            print('No data found')
        else:
            print("Keep in mind you cannot change either age, account number and balance.\n") 
            print("Please provide further new details.")
            new_data={
                'name': input('Enter new Name: '),
                'email': input("Enter new Email: "),
                'pin' : input("Enter new pin: ")
                }
            if new_data['name']=="":
                new_data['name']=userdata[0]['name']
            if new_data['email']=="":
                new_data['email']=userdata[0]['email']
            if new_data['pin']=="":
                new_data['pin']=userdata[0]['pin']
                
            new_data['age']=userdata[0]['age']
            
            new_data['accountno']=userdata[0]['accountno']
            new_data['balance']=userdata[0]['balance']
            
            if type(new_data['pin'])==str:
                new_data['pin']=int(new_data['pin'])
            for i in new_data:
                if new_data[i]==userdata[0][i]:
                    continue
                else:
                    userdata[0][i]=new_data[i]
            Bank.__update()
            print("Details updated successfully!")
    
    def delete(self):
        ac_no=input("Enter your account number: ")
        pin=int(input('Enter your pin: ')) 
        userdata=[i for i in Bank.data if i ['accountno']==ac_no and i['pin']==pin]
        if userdata==False:
            print('No record found')
        else:
            del_ac=input('Enter y for delete account or n')
            if del_ac=='n' and del_ac=='N':
                print("Ok move next")
            else:
                index=Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print('Account deleted successfully')
                Bank.__update() 
          
obj_bank=Bank()

print('Press 1 for creating account.')
print('Press 2 for depositing money.')
print('Press 3 for withdraw money.')
print('Press 4 for check details.')
print('Print 5 for update details.')
print('Press 6 for delete details.')
user_option=int(input('Please select option: '))

if user_option==1:
    obj_bank.create_account()
if user_option==2:
    obj_bank.depositmoney()
if user_option==3:
    obj_bank.withdraw()
if user_option==4:
    obj_bank.showdetails()
if user_option==5:
    obj_bank.updatedetails()
if user_option==6:
    obj_bank.delete()
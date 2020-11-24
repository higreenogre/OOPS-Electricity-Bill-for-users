#update: TRANSACTION MODULE
import pickle
import os
filename=input('Enter the file name with the path ')
class customer:
    def __init__(self): #INITIALIZE PROPERTIES
        self.accno=0
        self.name='Not Assigned'
        self.address='Not Assigned'
        self.phno=0
        self.occup='Not Assigned'
        self.region='Not Assigned'
        self.mr=0
        self.cost=0.0
        self.porup='Not Assigned'
    def input(self):
        valid1=False
        while not valid1:
            try:
                print('Customer Record #')
                valid=False
                while not valid:
                    try:
                        self.accno=int(input('     Enter the account number : '))
                        if self.getaccno()!=True:
                            valid=True
                        else:
                            print('This account already exists')
                    except ValueError:
                        print('invalid input')
                self.name=input('     Enter the name of the customer          : ')
                self.phno=int(input('     Enter the phone number of the customer  : '))
                self.address=input('     Enter the address of the customer       : ')
                valid2=False
                while not valid2:
                    try:
                        self.mr=int(input('     Enter the meter reading                 : '))
                        if self.mr>0:
                            valid2=True
                    except ValueError:
                        print('The entered detail is invalid. Please try again')
                if self.mr<=50:
                    self.cost=50.0
                elif self.mr<=1000:
                    self.cost=50.0+(self.mr-50)*1.5
                elif self.mr<=2000:
                    self.cost=50.0+950*1.5+(self.mr-1000)*1.75
                elif self.mr>2000:
                    self.cost=50.0+950*1.5+1000*1.75+(self.mr-2000)*2.0
                self.porup='UNPAID'
                valid1=True
            except ValueError:
                print('Enter correct values ')
        return True
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    def add_data(self,filename):#TO ADD NEW RECORD
        try:
            file=open(filename,'ab')
            file.close()
        except IOError:
            print('could not create file')
            return
        while True:
            file=open(filename,'ab')
            if self.input()==True:
                pickle.dump(self,file)
            file.close()
            ans=input('Add more y/n ')
            if ans.upper()=='N':
                break
        file.close()
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    def getaccno(self):#TO CHECK IF THE ACCOUNT IS DUPLICATE
        if os.path.isfile(filename):
            file=open(filename,'rb')
            c=customer()
            while True:
                try:
                    c=pickle.load(file)
                    if c.accno==self.accno:
                        file.close()
                        return True
                except EOFError:
                    break
            file.close()
        return False
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    def delete(self,filename): #DELETES THE RECORD FROM THE DATABASE
        if not os.path.isfile(filename):
            print('File does not exist')
            return
        file=open(filename,'rb+')
        file2=open('temp','wb+')
        valid=False
        while not valid:
            try:
                accno=int(input('     Enter the Account Number to be deleted  : '))
                valid=True
            except ValueError:
                print('Enter The Value Correctly')
        found=False
        while True:
            try:
                self=pickle.load(file)
                if self.accno==accno:
                    found=True
                else:
                    pickle.dump(self,file2)
            except EOFError:
                break
        file.close()
        file2.close()
        os.remove(filename)
        os.rename('temp',filename)
        if found:
            print('The Customer Record Was Deleted Successfully ')
        else:
            print('The Account Does Not Exist')

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    def modify(self,filename): #TO MODIFY THE EXISTING RECORD FROM THE DATABASE
        if not os.path.isfile(filename):
            print('File does not exist')
            return
        file=open(filename,'rb+')
        file2=open('temp','wb+')
        accno=int(input('     Enter the Account Number to be modified : '))
        found=False
        while True:
            try:
                self=pickle.load(file)
                if self.accno==accno:
                    valid1=False
                    while not valid1:
                        try:
                            out='''
    1. Do You Want To Modify Your Name Which Was %s
    2. Do You Want To Modify Your Phone Number Which Was %d 
    3. Do You Want To Modify Your Address Which Was %s
    4. Do You Want To Modify Your meter reading Which Was %d

    5. To Quit  '''
                            print(out%(self.name.upper(),self.phno,self.address.upper(),self.mr))
                            choice3=mychoice3()
                            if choice3==1:
                                self.name=input('Enter the name of the customer : ')
                            elif choice3==2:
                                self.phno=int(input('Enter the phone number of the customer : '))
                            elif choice3==3:
                                self.address=input('Enter the address of the customer : ')
                            elif choice3==4:
                                valid2=False
                                while not valid2:
                                    try:
                                        self.mr=int(input('Enter the meter reading : '))
                                        if self.mr>0:
                                            valid2=True
                                    except ValueError:
                                        print('The entered detail is invalid. Please try again')
                                if self.mr<=50:
                                    self.cost=50.0
                                elif self.mr<=1000:
                                    self.cost=50.0+(self.mr-50)*1.5
                                elif self.mr<=2000:
                                    self.cost=50.0+950*1.5+(self.mr-1000)*1.75
                                elif self.mr>2000:
                                    self.cost=50.0+950*1.5+1000*1.75+(self.mr-2000)*2.0
                                self.porup='UNPAID'
                            else:
                                break
                            valid1=True
                        except ValueError:
                            print('Enter The Values Correctly')
                    pickle.dump(self,file2)
                    found=True
                while self.accno!=accno:
                    pickle.dump(self,file2)
                    break
            except EOFError:
                break
        file.close()
        file2.close()
        os.remove(filename)
        os.rename('temp',filename)
        if found:
            print('The Customer Record Was Modified Successfully ')
        else:
            print('The Account Does Not Exist')

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    def showbill(self,filename):#SHOWS THE ELECTRICITY OF THE ENTERED ACCOUNT
        if not os.path.isfile(filename):
            print('File does not exist')
            return
        file=open(filename,'rb+')
        accno=int(input('Enter the Account Number : '))
        found=False
        while True:
            try:
                self=pickle.load(file)
                if self.accno==accno:
                    found=True
                    out="""
        ----------------------------------------------------------
          ACCOUNT NUMBER                  : %d
        ----------------------------------------------------------
          NAME OF CUSTOMER                : %s    
          PHONE NUMBER                    : %d
          ADDRESS                         : %s
          ELECTRICITY CHARGE              : Rs %f
          PAID/UNPAID                     : %s
        ----------------------------------------------------------"""
                    print(out%(self.accno,self.name.upper(),self.phno,self.address.upper(),self.cost,self.porup))
                    return
            except EOFError:
                break
        file.close()
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    def payment(self,filename):
        t=trans()
        if not os.path.isfile(filename):
            print('File does not exist')
            return
        file1=open(filename,'rb+')
        file2=open('temp','wb+')
        accno=int(input('Enter the Account Number : '))
        while True:
            try:
                self=pickle.load(file1)
                if self.accno==accno:
                    if self.porup=='PAID':
                        print('Your Bill Has Already Been Paid.')
                        break
                    found=True
                    print(self.name.upper(),' , Your Electricity Charge Is - Rs ',self.cost)
                    print("""How Would You Like Your Payment To Be IN?
                             press 1 if you are paying on cash
                             press 2 if you are paying by credit card""")
                    valid1=False
                    while not valid1:
                        try:
                            choice=int(input(''))
                            if choice==1:
                                valid2=False
                                while not valid2:
                                    try:
                                        money=float(input('enter the cash paid Rs '))
                                        if money>=self.cost:
                                            print('the balance is Rs ',money-self.cost,'\nThankyou!!!')
                                            cost=self.cost
                                            self.porup="PAID"
                                            t.writefile(accno,cost,'PAID')
                                            pickle.dump(self,file2)
                                            break
                                        else:
                                            print('not enough cash')
                                    except IOError:
                                        print('The value you entered is invalid')
                                valid1=True
                            elif choice==2:
                                print('Bill successfully paid by credit card \nThankyou!!!')
                                cost=self.cost
                                self.porup="PAID"
                                t.writefile(accno,cost,'PAID')
                                pickle.dump(self,file2)
                                break
                            else:
                                print('Invalid Choice')
                        except EOFError:
                            break
                else:
                    pickle.dump(self,file2)
            except EOFError:
                break
        file1.close()
        file2.close()
        os.remove(filename)
        os.rename('temp',filename)
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    def display_all(self,filename):
        if not os.path.isfile(filename):
                print('File does not exist')
                return
        file=open(filename,'rb+')
        found=False
        print("""
                                      ----------ALL CUSTOMER RECORDS----------
 ________________________________________________________________________________________________________________________
|ACC NO    |   NAME                  |   LANDLINE NUMBER    |   ADDRESS                    |   E-CHARGE    | PAID/UNPAID |
|__________|_________________________|______________________|______________________________|_______________|_____________|""")
        while True:
            try:
                self=pickle.load(file)
                found=True
                out="""|%-10d|%-25s|%-22d|%-30s|Rs %12.2f|   %-10s|
|__________|_________________________|______________________|______________________________|_______________|_____________|"""  

                print(out%(self.accno,self.name.upper()[:25],self.phno,self.address.upper()[:30],self.cost,self.porup[:10]))
            except EOFError:
                break
        file.close()
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    def report(self):#report menu
        t=trans()
        t.report()
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    def getnameaddress(self,accno):#to get the name,address,amount,status and balance
        if os.path.isfile(filename):
            file=open(filename,'rb+')
            while True:
                try:
                    self=pickle.load(file)
                    if self.accno==accno:
                        file.close()
                        return self.name.upper(),self.phno,self.address.upper(),self.porup
                except EOFError:
                    break
            file.close()
            return'','','','',''
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
import datetime
class trans:#to record all the transactions and generate reports
    def writefile(self,accno,cost,porup):#to create a transaction
        d=datetime.datetime.now()
        self.day=d.day
        self.month=d.month
        self.year=d.year
        self.accno=accno
        self.porup=porup
        self.cost=cost
        try:
            file=open('trans.dat','ab')
        except IOError:
            print('Cannot open transaction file')
            return
        pickle.dump(self,file)
        file.close()
    def report(self):#to display the reports for all deposits and all withdrawals
        out1="""
                       ALL %-10s FOR %02d/%4d
 ___________________________________________________________________________________________________________________________________
|ACC NO    |   DATE   |   NAME                  |   LANDLINE NUMBER    |   ADDRESS                    |   E-CHARGE    | PAID/UNPAID |
|__________|__________|_________________________|______________________|______________________________|_______________|_____________|"""


        out2="""|%-10d|%02d/%02d/%04d|%-25s|%-22d|%-30s|Rs %12.2f|%-13s|
|__________|__________|_________________________|______________________|______________________________|_______________|_____________|"""  
        
        c=customer()
        
        if os.path.isfile('trans.dat'):
            file=open('trans.dat','rb')
            valid=False
            while not valid:
                try:
                    month=int(input('Enter the month : '))
                    year=int(input('Enter the year : '))
                    if 1<=month<=12 and year>2000:
                        valid=True
                    else:
                        print('Invalid month or year')
                except ValueError:
                    print('Invalid input')
                print(out1%('RECORDS',month,year))
            while True:
                try:
                    self=pickle.load(file)
                    if self.month==month and self.year==year:
                        name,phno,address,porup=c.getnameaddress(self.accno)
                        print(out2%(self.accno,self.day,self.month,self.year,name[:25],phno,address[:30],self.cost,porup[:13]))
                except EOFError:
                    break
            file.close()

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
def electric_bill():
    out="""
    -------------------------------------------
    |           ELECTRICITY BILL MENU         |
    |           ---------------------         |
    |                                         |
    |  1. Append A Customer Record            |
    |  2. List Of Customers                   |
    |  3. report                              |
    |  4. Show Bill                           |
    |  5. Payment Of Bill                     |
    |                                         |
    |  6. To exit menu                        |
    -------------------------------------------"""
    print (out)
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
def Append():
    out="""
    -------------------------------------------
    |          APPEND CUSTOMER RECORD         |
    |          ----------------------         |
    |                                         |
    |  1. Add A Customer Record               |
    |  2. Delete A Record                     |
    |  3. Modify A Record                     |
    |                                         |
    |  4. To Quit                             |
    -------------------------------------------"""
    print (out)
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
def mychoice1():
    valid_input=False
    while not valid_input:
        try:
            choice1=int(input())
            if 1<=choice1<=6:
                valid_input=True
            else:
                print('Invalid choice')
        except ValueError:
            print('Invalid choice')
    return choice1
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
def mychoice2():
    valid_input=False
    while not valid_input:
        try:
            choice2=int(input())
            if 1<=choice2<=4:
                valid_input=True
            else:
                print('Invalid choice')
        except ValueError:
            print('Invalid choice')
    return choice2
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
def mychoice3():
    valid_input=False
    while not valid_input:
        try:
            choice3=int(input())
            if 1<=choice3<=5:
                valid_input=True
            else:
                print('Invalid choice')
        except ValueError:
            print('Invalid choice')
    return choice3
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    print (out)
def fileio():
    global filename
    valid_choice1=True
    e=customer()
    t=trans()
    while valid_choice1:
        electric_bill()
        choice1=mychoice1()
        if choice1==1:
            valid_choice2=True
            while valid_choice2:
                Append()
                choice2=mychoice2()
                if choice2==1:
                    e.add_data(filename)
                elif choice2==2:
                    e.delete(filename)
                elif choice2==3:
                    e.modify(filename)
                elif choice2==4:
                    break
        elif choice1==2:
            e.display_all(filename)
        elif choice1==3:
            e.report()
        elif choice1==4:
            e.showbill(filename)
        elif choice1==5:
            e.payment(filename)
        elif choice1==6: # EXITS PROGRAM
            print('Thank you !')
            return
if __name__=="""__main__""":
    fileio()


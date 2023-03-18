import json
from datetime import datetime
class ATM:
    def __init__(self,branch_name:str,json_path=None) -> None:
        """
        INPUT:
            1. branch_name: name of the branch
            2. json_path: if json already exists
        OUTPUT:
            1. json will be created
            2. json will be opened if it already exists
        """
        
        self.branch_name = branch_name

        if json_path:

            self.json_path = json_path
            with open(json_path) as json_file:
                self.bank = json.load(json_file)
        
        self.logged_in = False
        self.logged_in_user = ""
    
    def commit_changes(self):
        with open(self.json_path,'w') as update_file:
            json.dump(self.bank, update_file,indent=4)

            return True

    def create_acc(self,user_acc,password):
        # Add a new acc to the json, and add a transaction record showing date and time of creation
        # Password needs to be confirmed twice.
        # Can be taken in as input too.
        
        """
        Creates a new acc
        Appending a dictionary to the Accounts list in the atm json
        Structure
        
        {"Name":"asas","Password":"Something",Transactions:["Created at","Deposited","Withdrawn"]}
        Will also log the new user in.
        """


        timestamp = f"Created at {str(datetime.today())[:-7]}"
        person = {"username":user_acc,
                  "password":password,
                  "Balance":0,
                  "Transactions":[timestamp]}
        print(self.bank["Accounts"])
        self.bank["Accounts"][user_acc] = person

        self.commit_changes()


        self.logged_in = True
        self.logged_in_user = user_acc

        return ("Account Created",True)

    def login(self,user_acc,password):
        # check password in the json file and return true or false and change logged in state.
        # checking membership can be a bug
        if user_acc in  self.bank["Accounts"]:
            if self.bank["Accounts"][user_acc]['password'] == password:
                self.logged_in = True
                self.logged_in_user = user_acc

                return ("Logged in",True)
            
            else:
                return ("Incorrect Password",False) 
        else:
            return ("Not a Member",False)

    def logout(self):
        self.logged_in = False
        self.logged_in_user = ""

        return ("Logged Out",False) 

    def current_balance(self):
        if self.logged_in:
            return self.bank["Accounts"][self.logged_in_user]["Balance"]
    
    def deposit(self,amount):
        # use the self.logged_in_user, and add deposited amount, add timestamp to the transactions
        timestamp = f"Deposited {amount} at {str(datetime.today())[:-7]}"
        
        # Not logged in can be a bug
        if self.logged_in:

            self.bank["Accounts"][self.logged_in_user]['Balance'] += amount
            self.bank["Accounts"][self.logged_in_user]['Transactions'].append(timestamp)

    

            return ("Deposited",True)


    def withdraw(self,amount):
        # use self.logged_in_user, withdraw amount , add timestamp to transactions
        
        if self.logged_in:
            cur_balance = self.bank["Accounts"][self.logged_in_user]["Balance"]
            

            self.bank['Accounts'][self.logged_in_user]["Balance"] = cur_balance - amount
            self.commit_changes()
            return True
            
    def delete_acc(self,password):
        # can be done only if you're logged in, and will delete the acc.
        if self.logged_in:

            check_password = self.bank["Accounts"][self.logged_in_user]['password']

            if check_password == password:
                self.bank["Accounts"].pop(self.logged_in_user)
                
                self.logout()

                self.commit_changes()

                return True

            return False
        

if __name__ == "__main__":
    atm = ATM("Nigdi",'./Nigdi_atm.json',True)
    atm.create_acc("Virenn","pomos")
    atm.create_acc("Isha","popos")
    atm.create_acc("Aryan","momos")
    atm.create_acc("Keshwam","pomom")

    x = atm.login("Isha","popos")
    print(x)
    print(atm.logged_in_user)

    atm.deposit(4000)
    atm.withdraw(300)
    atm.withdraw(5000)
    atm.delete_acc()


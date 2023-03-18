from atm import ATM

JSON_PATH = './Venn_atm.json'
atm = ATM(branch_name='Venn',json_path = JSON_PATH)



# Main while loop.

while True:

    if not atm.logged_in:

        choices = ['login','create new acc','exit']
        choice = input(f"What do you want to do \n {', '.join(choices)}: ")

        if choice in choices:
            
            # executing function mapped to choice
            if choice == 'create new acc':

                user_acc = input("Enter your new user id: ")
                password = input("Enter your new password: ")
                confirm_password = input("Enter your password again: ")
                
                if confirm_password == password:
                    
                    response = atm.create_acc(user_acc,password)
                    if response[1] == True:
                        print("Account Created")
                        
                    else:
                        print("Password not the same, please try again")
            
            if choice == 'login':

                user_acc = input("Enter your user id: ")
                password = input("Enter your password: ")

                response = atm.login(user_acc,password)

                if response[1]:

                    # logged in submenu
                    pass

                else:
                    
                    print(response[0])
            
    
    if atm.logged_in:
        choices = ['current balance','deposit','withdraw','logout','delete_acc']


        choice = input(f"What do you want to do\n{' ,'.join(choices)}: ")

        if choice in choices:
            
            if choice == 'current balance':

                current_balance = atm.current_balance()
                print(f"Your current balance is: {current_balance}.")
            
            elif choice == "deposit":

                amount = int(input("Enter the amount you want to deposit: "))

                atm.deposit(amount)

                print(f"Deposited: Rs{amount}")
            
            elif choice == "withdraw":

                amount = int(input("Enter the amount you want to withdraw: "))

                response = atm.withdraw(amount)

                if response:
                    print("Please collect cash from Venn register")
                else:
                    print(f"Current balance insufficient: {atm.current_balance()}")
            
            elif choice == "logout":
                atm.logout()
                print("Logged out")
            
            elif choice == "delete_acc":
                print("You have chosen to delete your account.")
                password = input("Confirm your decision, by entering your password: ")

                response = atm.delete_acc(password)

                if response:
                    print("You account has been deleted! Bisss")
                else:
                    print("Wrong password, could not delete")

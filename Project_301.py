class bank:
    #deposite
    #withdraw
    bal = 0;
    def get_deposite(self):
        d1 = int(input('Enter the deposite amount : '))
        self.bal = self.bal + d1
        print("==================================")
        print("|Your deposit has been inserted.|")
        print("==================================")
        with open('History_file.txt','a') as w:
            w.write(f"\nYour deposit of {d1} has been inserted.\n==============================\n|Your balance is : {self.bal} |\n==============================")
            
        return self.bal
    def withDraw(self):
        w1 = int(input("Enter the amount to withdraw : "))
        if (w1>self.bal):
            print("====================================================")
            print(f"|No sufficient balance. (Balance is less than {w1})|")
            print("=====================================================")
        else:
            self.bal = self.bal - w1
            print("=============================================")
            print(f"|You have withdrawn {w1} from your account.|")
            print("=============================================")
            with open('History_file.txt','a') as w:
                w.write(f"\nYou have withdrawn {w1} from your account.\n==============================\n|Your balance is : {self.bal} |\n==============================") 
  
        return self.bal
    def show_bal(self):
        print("==============================")
        print("Your balance is : ", self.bal,"|")
        print("==============================")
    def read_hist(self):
        with open('History_file.txt', 'r') as r:
            print(r.read())
 


user = bank()

while True:
    print(" 1 to Deposit \n 2 to Withdraw \n 3 to Display the balance \n 4 to Display the history \n 5 to Log Out")
    try: 
        choice = input("Enter your choice : ")
        choice = int(choice)
        if(choice == 5):
            with open('History_file.txt','w') as v:
                v.write("")
            break
        elif(choice == 1):
            user.get_deposite()
        elif(choice == 2):
            user.withDraw()
        elif(choice == 3):
            user.show_bal()
        elif(choice == 4):
            print("**************This is your history file*******************")
            print("------------------xxxxxxxxxxxxxxxx------------------------\n")
            user.read_hist()
        else:
            print("==============================")
            print("|Enter the valid number only!|")
            print("==============================")
        
    except ValueError:
        print("======================")
        print("|Enter number only ! |")
        print("======================")
    # except Exception as e:
    #     print(type(e))

# user.get_deposite()
# user.withDraw()
# user.show_bal()


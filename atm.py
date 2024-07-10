class Atm:

    __counter = 1

    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.cid = Atm.__counter
        Atm.__counter = Atm.__counter + 1
        self.menu()

    @staticmethod
    def get_counter():
        return Atm.__counter
    
    def get_balance(self):
       return self.__balance 
    
    def set_balance(self,new_value):
        if type(new_value) == int:
            self.__balance = new_value
        else:
            print("Tu to gaya")
    
    def menu(self):
      
        user_input = input("""
            Hi how can I help you?
            1. Press 1 to create pin
            2. Press 2 to change pin
            3. Press 3 to check balance
            4. Press 4 to withdraw
            5. Anything else to exit
            """)

        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdraw()
        else:
            exit()

    def create_pin(self):
        user_pin = input('Enter the pin')
        self.pin=user_pin

        user_balance = int(input('Enter the balance'))
        print("Your balance is",user_balance)
        self.balance= user_balance

        print("Pin created sucessfully")
        self.menu()
    def change_pin(self):
        old_pin = input("Enter old pin")
        if self.pin == old_pin:
            change_pin = input('Enter new pin')
            self.pin = change_pin
            print("New pin created sucessfully")
            self.menu()

        else:
            print("Incorrect pin")
            self.menu()

    def check_balance(self):
        user_pin = input("Enter your Pin")
        if user_pin == self.pin:
            print("Your balance is", self.balance)
            self.menu()
        else:
            print("Enter correct pin")
            self.menu()
        
    def withdraw(self):
        user_pin = input("Enter your Pin")
        if user_pin == self.pin:
            amount = int(input("Enter the amount"))
            if amount <= self.balance:
                self.balance = self.balance - amount 
                print('Withdraw successfully',self.balance)
            else:
                print("sorry") 
        else:
            print("incorrect Pin    ")
        self.menu()

obj = Atm()
a = obj.get_balance()
print(a)
b = obj.set_balance("Hee")
print(b)
c = obj.withdraw()
print(c)
obj.cid()
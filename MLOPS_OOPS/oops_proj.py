class chatbook:
    def __init__(self):
        self.username=" "
        self.password=""
        self.loggedin=False
        self.menu()


    def menu(self):

        user_info=input("""Welcome tp checkbook.How would you like to proceed?
        
                        1.Press 1 to singup
                        2.Press 2 to singin
                        3.Press 3 to write a post
                        4.Press 4 to messege a friend
                        5.Press any other key to exit
                        """)

        if user_info=="1":
            self.signup()
        elif user_info=="2":
            self.signin()
        elif user_info=="3":
            pass
        elif user_info=="4":
            pass
        else:
            exit()
    def signup(self):
        self.username=input("Enter your username:")
        self.password=input("Enter your password:")
        print(f"Your account has been created successfully with username:{self.username} and password:{self.password}") 
        print("/n")
        self.menu()
    def signin(self):
        if self.username=="" and self.password=="":
            print("You have not created an account yet. Please create an account first.")
            self.menu()
        else:
            username=input("Enter your username:")
            password=input("Enter your password:")
            if username==self.username and password==self.password:
                print(f"Welcome back {self.username}!")
                self.loggedin=True
                self.menu()
            else:
                print("Invalid username or password. Please try again.")
                self.menu()


obj=chatbook()

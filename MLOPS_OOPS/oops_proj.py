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
            pass
        elif user_info=="2":
            pass
        elif user_info=="3":
            pass
        elif user_info=="4":
            pass
        else:
            exit()


obj=chatbook()

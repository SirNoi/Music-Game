from time import sleep
from game import Game

class login():
    """Login class which contains the login/sign-up methods"""

    #Lambda function to clear the console
    clear = lambda: print("\033c", end="", flush=True)

    def login_menu() -> None:
        """Allows the user to pick whether to login or sign-up"""

        menu_text = 'Welcome to the menu!\nPlease select one of these options:\nA: Login\nB: Signup\n'
        choice = input(menu_text)

        if choice.upper() == "A":
            login.login()
        elif choice.upper() == "B":
            login.signup()
        else:
            print("\nPlease pick a choice!")
            login.login_menu()
    
    def signup() -> None:
        """Allows the user to sign-up with a username and password. Stores the login data in a login.txt file"""
        
        username: str = str(input("\nPlease enter a username(longer than 4 characters): "))
        password: str = str(input("Please enter a password(longer than 4 characters): "))

        #Check to make sure login data is not blank or too short
        if (username == "" or password == "") or (len(username)<4 or len(password)<4):
            print("\nUsername or Password cannot be empty/shorter than 4 characters")
            login.signup()
        
        #try except block to catch any errors which might be produced from appending to the file.
        #login information stored in form username:password
        try: 
            with open("login.txt","a") as f:
                f.write(f"{username}:{password}\n")
            
            print("\nYou have successfully signed up! Please login now.\n")
            sleep(3)
            login.clear()
            login.login()
            #^clears the console and redirects to login
        except:
            print("\n An error has occured, please try again")
            login.login_menu()

    def login() -> None:
        """Allows the user to input their Username and Password and login if their details are correct"""

        username: str = str(input("Username: ").strip())
        password: str = str(input("Password: ").strip())

        #Reads all the login data and turns it into a list
        with open("login.txt","r") as f:
            login_data = f.readlines()
        
        #checks if provided information is in the login.txt file
        if (f"{username}:{password}\n") in login_data:
            print("Successfully logged in! The Music Game is now loading.")
            sleep(2)
            login.clear()
            
            #calls the main_loop() function and gives it the name of the user
            #and makes the default score 0
            Game.main_loop(0,username)

        #Makes the user retry logging in from the main menu(login/sign-up)
        else:
            print("Login details were not found, please sign-up or try to login again.")
            sleep(2)
            login.clear()
            login.login_menu()
    
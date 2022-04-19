import time
import subprocess
from guizero import App, Text, Combo, PushButton, Window, Picture, CheckBox

#Passwords
#Hayley
HSPassword = ("Hayley Scott")
#Emma
ESPassword = ("Emma Smitten")
#London
LEPassword = ("London Eaton")
#Admin
ADPassword = ("Root Child")

File = open("Errors_SpaceOS.txt", "a")
File.write("SpaceOS booted no Errors yet...\n")
File.close()

def Login():
    app.hide()
    tourWindow = Window(app, title="Tour")
    Welcome = Text(tourWindow, text="Welcome to SpaceOS lets take a tour!")
    
    def NEXT1():
        tourWindow.hide()
        Usernamewindow = Window(tourWindow, title="Your username!", height=500, width=1080)
        Thisis = Text(Usernamewindow, text="This is your username you can not change it inless you know how to code!")
        SPACE = Text(Usernamewindow, text="     ")
        USERNAMETEXT = Text(Usernamewindow, text=Username)
        
        def NEXT2():
            Usernamewindow.hide()
            Tour2 = Window(Usernamewindow, title="Tour Page 2", height=500, width=1080)
            Hey = Text(Tour2, text="If you wish to exit the program you can't right now.")
            
            
            def Exit():
                HomeOS = Window(Tour2, title="Home", height=500, width=1000)
                Text001 = Text(HomeOS, text="Welcome " + Username + " to the home menu!")
                
                def SNAKE():
                    subprocess.call("python SpaceOS/snake.py")
                
                Snake = PushButton(HomeOS, text="Snake", command=SNAKE)
                
                Tour2.hide()
                
                def Googles():
                    Google = Window(HomeOS, title="Googles", height=500, width=1000)
                    WELCOMESCREEN = Text(Google, text="Welcome to Googles of the chrome(Not REAL GOOGLE)")
                    Image1 = Picture(Google, image="SpaceOS/Nice.jpg", height=500, width=700)
                    
                    def ENTER():
                        Images = Window(Google, title="Google Images", height=500, width=1000)
                        
                        Google.hide()
                    
                    Enter = PushButton(Google, text="Enter", command=ENTER)
                    
                    HomeOS.hide()
                    
                
                App_1 = PushButton(HomeOS, text="Googles", command=Googles)
            
            Close = PushButton(Tour2, text="Home", command=Exit)
        
        Page2 = PushButton(Usernamewindow, text="Next", command=NEXT2)
    
    Next1 = PushButton(tourWindow, text=("Next"), command=NEXT1)

print("Would you like to Start SpaceOS?")
print("Y/N")
YESORNO = input()


#if answer yes boot SpaceOS
if YESORNO == ('y'):
    Username = input("What do you want your user name to be? ")
    
    File = open("SpaceOS/Errors_SpaceOS.txt", "a")
    File.write("Logged in as \n")
    time.sleep(0.1)
    File.write(Username)
    File.write("\n")
    File.close
    
    
    if Username == ("London"):
        Lpassword = input("London's Password: ")
        
        if Lpassword == (LEPassword):
            print("Welcome London to SpaceOS!")
            print("Idk what else to put for your thing bc i have other things as well")
            print("Like Hayley, Emma, Admin(my acounnt)")
        else:
             print("\033[1;31;40m Worng Password")
             print("\033[1;37;40m")
             File = open("SpaceOS/Errors_SpaceOS.txt", "a")
             File.write("London's's Password Worng\n")
             File.close
             exit()
             
    if Username == ("Emma"):
           Epassword = input("Emma's Password: ")
           
           if Epassword == (ESPassword):
               print("Welcome Emma!")
               print("would you like to be an admin?")
               JOE = input("Y/N")
               if JOE == ("n"):
                   print("Oh ok")
                   exit()
                   
               if JOE == ("y"):
                   print("Ha yeah no only the people with the admin passwrod can be admin.")
                   print("Well anyway this took way to long to make soo yeah i wonder what i'm")
                   print("Gonna do with it because at the moment that i am coding this part of it")
                   print("I have nothing to do.")
                   exit()
           else:
               print("\033[1;31;40m Worng Password")
               print("\033[1;37;40m")
               File = open("SpaceOS/Errors_SpaceOS.txt", "a")
               File.write("Emma's Password Worng\n")
               File.close
               exit()
    
    if Username == ("Hayley"):
        rpassword = input("Hayley's password: ")
        
        if rpassword == (HSPassword):
            print("Welcome Hayley!")
            print("Welcome To SpaceOS")
            print("How are you?")
            question001 = input()
            
            if question001 == ("good"):
                print("Cool Cool Cool")
                
            if question001 == ("meh"):
                print("Oh")
            
            if question001 == ("bad"):
                print("OOF")
        else:
            print("\033[1;31;40m Worng Password")
            print("\033[1;31;40m")
            File = open("SpaceOS/Errors_SpaceOS.txt", "a")
            File.write("Hayley's Password Worng")
            File.close
            exit()     
               
    if Username == ("Admin"):
        password = input("Admin Password: ")
        if password == (ADPassword):
            print("Welcome Admin")
            print("What would you like to do?")
            CHANGE = input()
            
            if CHANGE == ("Emma Smitten"):
                print("Hey Emma i have something to tell you!")
                yorn = input("Do you want to hear what he has to say? Y/N")
                if yorn == ("y"):
                    subprocess.call("python SpaceOS/Nice.py")
                    exit()
            
            if CHANGE == ("Admin Panel"):
                
                def close():
                    exit()
                    
                #admin panel
                print("Opening Admin Panel...")
                time.sleep(2)
                AdminPanel = App(title="Admin Panel", height = 500, width=1000)
                Welcome = Text(AdminPanel, text="Welcome Admin!")
                Useragreement = Text(AdminPanel, text="End user agreement: do you acept us using your data to make this Program better?")
                Agree = CheckBox(AdminPanel, text="Agree")

                if Agree.value == 1:
                    print("UwU Girls Ahead")
                
                Close = PushButton(AdminPanel, text="Exit", command=close)
                
            if CHANGE == ("Boot SpaceOS"):
                print("ok starting now")
                time.sleep(2)
            if CHANGE == ("password"):
                print("What would you like to chnage your password too?")
                NEWPASSWORD = input()
                print("Your new password is " + NEWPASSWORD)
                print("Would you like to edit it?")
                print("Y/N")
                cp = input()
                if cp == ("y"):
                    print("what would you like to chnage it too?")
                    
                if cp == ("n"):
                    print("Type in your new password one more time for it to be locked into the system")
                    TYPED = input()
                    if TYPED == (NEWPASSWORD):
                        print("New password locked into the system")
                        time.sleep(1)
                        print("Would you like to boot SpaceOS?")
                        print("Y/N")
                        OUIORNON = input()
                        if OUIORNON == ("y"):
                            print("Ok")
                            
                        if OUIORNON == ("n"):
                           exit()
                            
        else:
            #if admin Password worng
            print("\033[1;31;40m Admin Worng Password")
            print("\033[1;37;40m")
            Username = "User"
            File = open("SpaceOS/Errors_SpaceOS.txt", "a")
            File.write("Password Worng swaped to User\n")
            File.close   
            exit()   
                                                
    print("Booting Now...")
    time.sleep(1)
    print("You got games on yo phone?")
    time.sleep(0.2)
    print("All is well...")
    time.sleep(0.3)
    print("Hey Man")
    time.sleep(0.3)
    print("Ha Ha Yes!")
    time.sleep(0.3)
    print("AYO?!")
    time.sleep(0.3)
    print("Ha Got Em")
    time.sleep(0.2)
    print("Elon Musk")
    time.sleep(0.3)
    print("Hey You!!")
    time.sleep(0.3)
    print("Made By Whyufollowme!!")
    time.sleep(0.5)
    print("OMG there are so many bugs please fix me PLease")
    time.sleep(0.5)
    print("Hey Man")
    time.sleep(0.4)
    print("Almost done booting SpaceOS...")
    time.sleep(0.3)
    print("To may lines of code")
    time.sleep(0.3)
    print("Alright the boot is done!")
                          
    app = App(title="SpaceOS Login", height=500, width=1080)                       
    Logintext = Text(app, text="Welcome to SpaceOS!")
    PICKUSER = Combo(app, options=[Username, "User 2"])
    LoginButton = PushButton(app, text=("Log in"), command=Login)

    
#if answer no don't boot SpaceOS
if YESORNO == ('n'):
    print("Ok Exiting now")
    File = open("SpaceOS/Errors_SpaceOS.txt", "a")
    File.write("SpaceOS Shut Down \n")
    File.close 
    time.sleep(1)
    exit()

app.display()
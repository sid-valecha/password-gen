import string
import random
import time

length = 0
letters = False
digits = False
punctuation = False
charsList = ""

#ask user for length
def welcome():
    global length
    print("Hello there, Padawan! I see you're in search of a new password for the JediNet, and let me assure you that you've come to the right place.\nI was trained personally by the resistance's esteemed IT department to create the most secure passwords to keep the Galaxy safe.\nSo let's get to business.")
    time.sleep(1)
    length = int(input("How many characters do you want this password to be? "))


#find out user preferences
def user_choices():
    global letters
    global digits
    global punctuation

    choices = input("""What kind of characters do you wish to have in your password?
                    1. letters
                    2. digits
                    3. punctuation
                    4. exit
                    You can choose a single one, or a combination of two, or all 3. enter the corresponding digits without any whitespaces between them.
                    If you changed your mind and do not need a password, you can enter 4 to exit the program.\n""")
   

    valid_choices = {'1', '2', '3', '4'}
    
    if not set(choices).issubset(valid_choices) or len(choices) == 0:
        print("Invalid input detected. Please enter a combination of 1, 2, 3, or 4 without spaces.")
        user_choices()  #recursively call user_choices if invalid input
    
    else:
        if '1' in choices:
            letters = True
        if '2' in choices:
            digits = True
        if '3' in choices:
            punctuation = True
        if '4' in choices:
            print("Goodbye, Padawan. May the force be with you.")
            exit()
    


#set up charsList depending on users preferences
def chars_selection():
    global charsList
    if letters:
        charsList += string.ascii_letters
    if digits:
        charsList += string.digits
    if punctuation:
        charsList += string.punctuation


def generate_password(length):
    password = []
    
    # make sure at least 1 of each selected character type is included
    if letters:
        password.append(random.choice(string.ascii_letters))
    if digits:
        password.append(random.choice(string.digits))
    if punctuation:
        password.append(random.choice(string.punctuation))

    while len(password) < length:
        randomChar = random.choice(charsList)
        password.append(randomChar)
    random.shuffle(password)
    print("Your randomly generated password is: " + "".join(password) + "\n")


#main function
def main():
    welcome()
    user_choices()
    time.sleep(1)
    print("Great! Let me get to work...\n")
    chars_selection()
    time.sleep(1)
    generate_password(length)
    print("Thanks for visiting me, Padawan. I hope to see you soon.")

#calling main
if __name__ =="__main__":
    main()
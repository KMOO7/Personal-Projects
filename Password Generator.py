import random
import time
import string
password_length=16

def generate_password():
    # Ensure at least one character from each category
    uppercase_letter=random.choice(string.ascii_uppercase)
    lowercase_letter=random.choice(string.ascii_lowercase)
    digit=random.choice(string.digits)
    special_characters=random.choice('!@#$%^&*()_-+={[}]|:;"\'<,>.?/')

    remaining_length=password_length-4 
    #-4 becz above varriable ensure one of each as per standards in password which fill up 4 character space in password 

    #Adds all kind of neccesary types into one varribale which can be use again to generate multiples of it. 
    all_char=uppercase_letter+lowercase_letter+digit+special_characters

    password=all_char+"".join(random.choice(all_char) for _ in range(remaining_length))

    # Shuffle the password to enhance randomness and for same covert password string to list as shuffle function is possible with list only becz of its mutable feature
    list_password=list(password)
    random.shuffle(list_password)
    final_password=''.join(list_password)
    return final_password

def main():
    print("Welcome to Password Generator Software")
    input("Press Enter to generate your password:")
    print("Generatimg your password.", end="")

    for _ in range(5):
        time.sleep(0.5)
        print(".",end="", flush=True)

    print("\nYour secured password is: " +generate_password())
    

if __name__== "__main__":
    main()

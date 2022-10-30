import os
import sys

def main():
    print("\nEmail Slicer Menu: \n1. Slice Username and Domain from a email address\n2. Create a email address from a username and domain name\n3. Exit")
    
    option = int(input("\nOption: "))

    if option == 1:
        option1()
    elif option == 2:
        option2()
    else:
        option3()

def option1():

    email = input("\nEmail: ").strip()

    username, domain = email.split("@")

    print(f"\nThe username is: {username} and the domain is: {domain}\n")

    os.system("pause")
    os.system("cls")
    return main()

def option2():
    
    user = input("\nUsername: ")
    domain = input("Domain: ")

    print(f"\nYour email address is: {user}@{domain}")

    os.system("pause")
    os.system("cls")
    return main()

def option3():
    sys.exit()

if __name__ == "__main__":
    main()
from Customer import customer_main
from Agent import agent_main
import database

def main():
    while True:
        print("")
        print("Welcome to this Bank Management App!")
        print("0. Exit")
        print("1. Customer")
        print("2. Agent")
        choice = input("Please choose an option: ")
        if choice == "1":
            customer_main()
        elif choice == "2":
            agent_main()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


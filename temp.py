import json
import time


print("\n" + "="*55)
print("\t\t📚 LIBRARY MANAGEMENT SYSTEM")
print("="*55 + "\n")
USER_FILE = "users.json"
BOOKS_FILE = "books.json"

logged_in_user = None

# ... [Keep all your existing functions exactly the same until the main menu] ...

# Main Menu Loop
while True:
    if logged_in_user is not None:
        print("\n" + "-"*55)
        print(f"\t\t\tWELCOME BACK, {logged_in_user.upper()}!")
        print("-"*55)

    print("\n" + "="*25 + " MAIN MENU " + "="*25)
    print("\t1. Login")
    print("\t2. Register")
    print("\t3. Search Book")
    print("\t4. Borrow Book")
    print("\t5. Check Availability")
    print("\t6. Add Books (Admin Only)")
    print("\t7. Grant Admin Access (Admin Only)")
    print("\t8. View User History")
    print("\t9. Exit")
    print("="*61 + "\n")

    try:
        choice = int(input("| Enter your choice (1-9): "))
    except ValueError:
        print("\n" + "!"*55)
        print("  INVALID INPUT - PLEASE ENTER A NUMBER BETWEEN 1-9")
        print("!"*55 + "\n")
        continue

    if choice == 1:
        print("\n" + "-"*55)
        print("\t\t\tLOGIN PORTAL")
        print("-"*55)
        login()
    elif choice == 2:
        print("\n" + "-"*55)
        print("\t\t\tREGISTRATION PORTAL")
        print("-"*55)
        register()
    elif choice == 3:
        print("\n" + "-"*55)
        print("\t\t\tBOOK SEARCH")
        print("-"*55)
        search_query = input("\n| Enter book title or author to search: ")
        search_book(search_query)
    elif choice == 4:
        print("\n" + "-"*55)
        print("\t\t\tBOOK BORROWING")
        print("-"*55)
        borrow_query = input("\n| Enter book title or author to borrow: ")
        borrow_book(borrow_query)
    elif choice == 5:
        print("\n" + "-"*55)
        print("\t\tAVAILABILITY CHECK")
        print("-"*55)
        check_query = input("\n| Enter book title or author to check: ")
        check_availability(check_query)
    elif choice == 6:
        print("\n" + "="*55)
        print("\t\tADMIN PORTAL - ADD NEW BOOKS")
        print("="*55)
        print("\n" + "-"*55)
        login()
    elif choice == 7:
        print("\n" + "="*55)
        print("\tADMIN PORTAL - GRANT USER ACCESS")
        print("="*55)
        grantaccess()
    elif choice == 8:
        print("\n" + "="*55)
        print("\t\tUSER HISTORY PORTAL")
        print("="*55)
        history()
    elif choice == 9:
        print("\n" + "="*55)
        print("\tTHANK YOU FOR USING LIBRARY MANAGEMENT SYSTEM!")
        print("\t\t      GOODBYE!")
        print("="*55 + "\n")
        break
    else:
        print("\n" + "!"*55)
        print("  INVALID CHOICE - PLEASE ENTER A NUMBER BETWEEN 1-9")
        print("!"*55)

    # Add space between iterations
    print("\n" + "_"*55 + "\n")
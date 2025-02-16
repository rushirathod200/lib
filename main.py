import json
import time



print("\n" + "="*55)
print("\t\t📚 LIBRARY MANAGEMENT SYSTEM")
print("="*55 + "\n")
USER_FILE = "users.json"
BOOKS_FILE = "books.json"

logged_in_user = None

def register():
    try:
        with open(USER_FILE, "r") as file:
            users = json.load(file)
        
    except (FileNotFoundError, json.JSONDecodeError):
        users = {}

    username = input("Enter new username: ")
    password = input("Enter new password: ")

    if username in users:
        print(" Username already exists!")
        return

    users[username] = password
    users["history"][username]={}
    users["history"][username]["books"]=[]
    with open(USER_FILE, "w") as file:
        json.dump(users, file, indent=4)

    print("User registered successfully!")
    time.sleep(2)

# Function to login
def login():
    global logged_in_user
    if logged_in_user is not None:
        print("user is already logged in")
        return
    try:
        with open(USER_FILE, "r") as file:
            users = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        users = {}
    print("Please login yourself!")
    time.sleep(2)
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username] == password or users[username]["password"] == password:
        if username == 'admin' and users[username] == 'admin123':
            print("welcome admin")
            time.sleep(2)
            if choice == 6:
                addbook()
                return
            if choice == 7:
                grantaccess()
                return
        else:
            logged_in_user = username
            print(f"Welcome, {username}!")
        
    else:
        print("Invalid username or password")

def search_book(query):
    try:
        with open(BOOKS_FILE, "r") as file:
            books = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print(" No books available!")
        return

    results = [book for book in books if query.lower() in book["title"].lower() or query.lower() in book["author"].lower()]
    
    if results:
        print("🔍 Search Results:")
        for i, book in enumerate(results, start=1):
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - Copies: {book['copies']}, Available: {book['available']}")
    else:
        print(" No books found matching your search!")
    time.sleep(3)
def addbook():
    if not logged_in_user:
        print("You must log in first!")
        time.sleep(2)
        return
    if logged_in_user is not 'admin':
        print("You must be an admin to add books!")
        time.sleep(2)
        return
    
    book_name=input("Book Name: ")
    with open(BOOKS_FILE, "r") as file:
        books = json.load(file)

    if any(book_name == book["title"] for book in books):
        print("Book already exists!")
        return
    else:
        book = {
            "title": book_name,
            "author": input("Author Name"),
            "year": int(input("Year of Publication")),
            "copies": int(input("Number of Copies")),
            "available": int(input("Number of Available Copies")),
        }
        
        books.append(book)
        with open(BOOKS_FILE, "w") as file:
            json.dump(books, file, indent=4)
        print(f'{book_name} is added successfully')
        time.sleep(2)
        

def borrow_book(query):
    if not logged_in_user:
        print("You must log in first!")
        return

    try:
        with open(BOOKS_FILE, "r") as file:
            books = json.load(file)
        
        with open(USER_FILE, "r") as file:
            user=json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print(" No books available!")
        return

    for book in books:
        if query.lower() in book["title"].lower() or query.lower() in book["author"].lower():
            if book["available"] > 0:
                book["available"] -= 1
                book.setdefault("borrowers", []).append(logged_in_user)
                if not isinstance(user["history"][logged_in_user]["books"], list):
                    user["history"][logged_in_user]["books"] = []
                user["history"][logged_in_user]["books"].append(str(book["title"]))

                with open(BOOKS_FILE, "w") as file:
                    json.dump(books, file, indent=4)
                with open(USER_FILE, "w") as file:
                    json.dump(user, file, indent=4)

                print(f" {book['title']} borrowed successfully!")
                return
            else:
                print(f" {book['title']} is not available!")
                return

    print(" Book not found!")

def return_book(){
     if not logged_in_user:
        print("You must log in first!")
        return
    try:
        with open(BOOKS_FILE, "r") as file:
            books = json.load(file)
        
        with open(USER_FILE, "r") as file:
            user=json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print(" No books available!")
        return

        if 

    

}

def check_availability(query):
    try:
        with open(BOOKS_FILE, "r") as file:
            books = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print(" No books available!")
        return

    for book in books:
        if query.lower() in book["title"].lower() or query.lower() in book["author"].lower():
            if book["available"] > 0:
                print(f" {book['title']} is available with {book['available']} copies left.")
            else:
                print(f" {book['title']} is fully occupied! Borrowers: {', '.join(book.get('borrowers', []))}")
            return
    time.sleep(3)

    print(" Book not found!")
def grantaccess():
    if logged_in_user is None:
       login()
    if logged_in_user is not 'admin':
        print("You must be an admin to add books!")
        time.sleep(2)
        return
    with open(USER_FILE,"r")as file:
        user=json.load(file)
    gnuser=input("Enter username to provide access:")
    if gnuser  in user["admin"]["access"]:
        print(f"{gnuser} already has access")
        return
    else:
        if gnuser in user:
            user["admin"]["access"].append(gnuser)
            print("Access granted. ")
            time.sleep(2)
        else:
            print("User not found")
            time.sleep(2)
            return
    with open(USER_FILE, "w") as file:
        json.dump(user, file, indent=4)


def history():
    if logged_in_user is None:
        login()
    with open(USER_FILE, "r") as file:
        user=json.load(file)
    uu=input("enter username to search")
    if uu in user:
        print(user["history"][uu]["books"] )

    else:
        print("User not found")
        return
    time.sleep(3)


    

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
        addbook()
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

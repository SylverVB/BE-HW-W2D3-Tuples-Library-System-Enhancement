# 1. Tuple Mastery in Python
# Objective:
# The aim of this assignment is to deepen your understanding of tuples in Python, along with their interaction with lists, 
# dictionaries, and basic Python functionalities like functions, input handling, and string formatting. By completing this 
# assignment, you will enhance your skills in data structuring, manipulation, and application of tuples in practical scenarios.

# Task 1: Formatting Flight Itineraries
# Create a Python function that takes a list of tuples as an argument. Each tuple contains information about a flight itinerary: 
# (traveler_name, origin, destination). The function should format and return a string that lists each itinerary. For example, if 
# the input is [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")], the output should be a string formatted as:
# "Itinerary 1: Alice - From New York to London
#  Itinerary 2: Bob - From Tokyo to San Francisco"


def flight_itinerary(passengers):
    print("\nThe information about flight itineraries:\n")

    for index, (traveler_name, origin, destination) in enumerate(passengers):
        print(f'Itinerary {index + 1}: {traveler_name} - From {origin} to {destination}')
    
    return passengers

passengers = [("Alice", "New York", "London"), ("Bob", "Tokyo", "London"), ("Victor", "Philadelphia", "Miami")]
flight_itinerary(passengers)

print("\n===============================================")

# 2. Python Data Structure Challenges in Real-World Scenarios
# Objective:
# This assignment is designed to enhance your understanding and application of Python's core data structures - tuples, lists, and 
# dictionaries - in real-world contexts. By engaging with these tasks, you will practice manipulating these data structures, 
# applying built-in Python methods, and implementing error handling in practical situations.

# Task 1: Library System Enhancement
# Sharpen your skills in managing and modifying data within tuples and lists.

# Problem Statement:
# You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by 
# adding new books and ensuring no duplicates.

# Existing Library Data:

# library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
#  - Add functionality to insert new books into library.
#  - Ensure that adding a duplicate book is handled appropriately.

def add_book(library):

    name = input("\nWhat is the name of the book you would like to add to your library? \n").lower()
    author = input("\nWho is the author of this book? \n").lower()
    
    if (name, author) in library:
        print("\nThis book is already in your library!\n")
    else:
        library.append((name, author))

    return library


def library_system():
    # Initialize an empty dictionary to store service tickets
    existing_library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
    library = [tuple(item.lower() for item in book) for book in existing_library]   # Convert the library items to lower case so that we can compare them

    while True:
        print("\nWelcome to our Library System!")
        print("\nMenu:")
        print("1. Add a new book")
        print("2. Quit")

        choice = input("\nWhat would you like to do? Enter your choice from 1 to 2: \n")
        if choice == "1":
            library = add_book(library)
            updated_library = [tuple(item.title() for item in book) for book in library]    # Convert the library items back to title()
            print("\n")
            print(updated_library, "\n")
        elif choice == "2":
            print("\nThank you for using our library!\n")
            break
        else:
            print("\nPlease enter a valid response!\n")
# Call the main function to start the program
library_system()

print("===============================================\n")

# 3. Mastering Tuple Packing and Unpacking in Python
# Objective: The goal of this assignment is to deepen your understanding of tuple packing and unpacking in Python. You will apply these techniques in various
# practical scenarios, enhancing your ability to work with flexible data structures and improve data handling efficiency.

# Task 1: Customer Order Processing Refine your skills in tuple unpacking by managing customer orders.

# Problem Statement: You are given a list of tuples, each representing a customer's order. Each tuple contains the customer's name, the product ordered, and 
# the quantity. Your task is to unpack each tuple and print the order details in a user-friendly format.

# Sample Order Data:

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Victor", "Monitor", 5)
]

print("Customer orders:\n")

for name, product, quantity in orders:
    print(f"{name}: {product} - {quantity}")

print("\n")


# Tuple Mastery in Python

# Task 1 : Formatting Flight Itineraries

flight_itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]

def tup_loop(itineraries):
    i = 1
    for itinerary in itineraries:
        # print(itinerary, type(itinerary))

        print(f"Itinerary {i}: {itinerary[0]} - From {itinerary[1]} - To {itinerary[2]}")
        i += 1

tup_loop(flight_itineraries)
flights = [("Frank", "Boston", "Detroit"), ("Jason", "Ohio", "North Carolina")]

tup_loop(flights)

# Python Data Structure Challenges in Real-World Scenarios

# Task 1: Library System Enhancement

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def menu():
    while True:
        input1 = input(''' 
Library of Books
                       
1- add a book
2- view books
3- quit
 ''')
        if input1 == "1":
            add()
        elif input1 == "2":
            print(library)
        elif input1 == "3":
            break
        else:
            continue

def add():
    input1 = input("What book would you like to add to the library?").title().lstrip().rstrip()
    for title,author in library:
        if input1 == title:
            print("Book already exists in library. Please enter another book.") 
            return

    input2 = input("Who is the author of the book?").title().lstrip().rstrip()
    new_book = input1, input2
    library.append(new_book)

menu()
        
    
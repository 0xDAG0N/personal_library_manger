'''
Personal library manger application
'''

# Imports
import json


# Class for personal library system
class PersonalLibrarySystem:
    # Constructor
    def __init__(self):
        self.books = []
        self.load_library()

    # Method to save library
    def save_library(self):
        try:
            with open('library.json', 'w') as file:
                json.dump(self.books, file)
            print("Library saved successfully!")
        # Handle exceptions
        except Exception as e:
            print(f"An error occurred while saving the library: {e}")

    # Method to load library
    def load_library(self):
        try:
            with open('library.json', 'r') as file:
                self.books = json.load(file)
            print("Library loaded successfully!")
        # Handle exceptions
        except FileNotFoundError:
            print("No library file found. Starting with an empty library.")
            self.books = []
        except json.JSONDecodeError:
            print("Error decoding the library file. Starting with an empty library.")
            self.books = []

    # Method to add book
    def add_book(self):
        name = input("Enter the name of the book: ")
        author = input("Enter the author of the book: ")
        category = input("Enter the category of the book: ")
        
        new_book = {'title':name,'author':author, 'category':category}
        self.books.append(new_book)
        self.save_library()
        print("Book added successfully")

    # Method to visualize library
    def visualize_library(self):
        categories_list = [cate["category"] for cate in self.books]
        used_cats = []
        # Print the categories and the number of books in each category
        max_length = max([len(cat) for cat in categories_list], default=0)
        print("--------------------------------------------------")
        for cat in categories_list:
            if cat not in used_cats:    
                counter = categories_list.count(cat)
                print(f'{cat.ljust(max_length)} ({counter}): {"*" * counter}')
                used_cats.append(cat)
        print("--------------------------------------------------")

            
# Main function
def main():
    print("Welcome to my personal library manger!")

    # Create a personal library system object
    library_system = PersonalLibrarySystem()

    # Main loop
    while True:
        print("""
            What would you like to do?
            1. add book
            2. Save library to file
            3. Load library from file
            4. Visualize library by category
            5. Quit
            """)
        # Get user choice
        choice = int(input("Enter choice: "))

        # Perform action based on user choice
        if choice == 1:
            library_system.add_book()
        elif choice == 2:
            library_system.save_library()
        elif choice == 3:
            library_system.load_library()
        elif choice == 4:
            library_system.visualize_library()
        elif choice == 5:
            print("Exiting program Bye !")
            break
        else:
            print("Enter valid choice")

            print("Thank you for using our library manger")

# Entry point of the program
if __name__ == '__main__':
    main()

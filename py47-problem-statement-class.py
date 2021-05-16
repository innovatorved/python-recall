# python3 py47-problem-statement-class.py
# Create a library Class

class Lib:
    def __init__(self , list_book, lib_name):
        self.books = list_book
        self.libName = lib_name
        self.issue_dict = {}
        self.donate = {}

    @property   
    def printbooks(self):
        return self.books

    def book_issue(self , book_name , name):
        # print(book_name)
        if book_name in self.books:
            # print("yes")
            self.issue_dict[book_name] = name
            del self.books[self.books.index(book_name)]
            return f"Book Issued to {name}"

        elif book_name in self.issue_dict:
            return (f"Book Already issued to :{self.issue_dict[book_name]}")

        else:
            return "Book is Not in Library"

    def book_donate(self , name, book_name):
        self.books.append(book_name)
        self.donate[book_name] = name
        return f"Thnkqq for Your Dobnation Mr. {name}"


    def return_book(self ,book_name) :
        del self.issue_dict[book_name]
        self.books.append(book_name)
        return f"Thnqq if you like pls Visit our lib {self.libName} Again"


if __name__ == "__main__":
    book_shell = Lib(["a" , "b" , "c"] , "yes")

    print(book_shell.book_issue("a" , "ved"))

    print(book_shell.issue_dict)
    print(book_shell.printbooks)
    
    print(book_shell.book_donate("Ved Gupta" , "Iris of India"))
    print(book_shell.printbooks)

    print(book_shell.book_issue("Iris of India" , "dev"))
    print(book_shell.printbooks)

    print(book_shell.return_book("Iris of India"))


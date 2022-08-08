class Liberary:
    bookLi = ["Rich Dad Poor Dad","Think and Grow Rich"]
    def showLBooks(self):
        for i ,item in enumerate(l.bookLi):
            print(f"{i}. {item}")
class student:
    bBooks = []
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def getData(self):
        print(self.name + " ",str(self.age))
    def borrowBook(self,bookName):
        book = l.bookLi[bookName]
        # print("Book " + book)
        if l.bookLi[bookName]:
            self.bBooks.append(book)
            l.bookLi.remove(book)
        else:
            print("Book Doesn't Exists!")
    def returnBook(self,bookName):
        book = self.bBooks[bookName]
        if self.bBooks[bookName]:
            self.bBooks.remove(book)
            l.bookLi.append(book)
        else:
            print("Book Doesn't Belong to U!")
    def showMyBooks(self):
        if len(self.bBooks)==0:
            print("Don't have Books")
        else:
            for i ,item in enumerate(self.bBooks):
                print(f"{i}. {item}")


name = input("Enter Ur Name:")
age = int(input("Enter Ur Age:"))
s1 = student(name,age)
l = Liberary()
print(("*"*10)+"Welcome To LMS"+("*"*10))
print(f"Name:{name}\nAge:{age}\n")
while True:
    choice = int(input(f"Enter Your Choice:\n1.Show Libarary Books\n2.Show My Borrow Books\n3.Borrow Book\n4.ReturnBook\n5.Exit:   "))
    if choice == 1:
        l.showLBooks()
    elif choice == 2:
        s1.showMyBooks()
    elif choice == 3:
        for i ,item in enumerate(l.bookLi):
            print(f"{i}. {item}")
        bookName = int(input("Enter Book You want:"))
        b = l.bookLi[bookName]
        s1.borrowBook(bookName)
        print(f"{b} Book Borrowed")
    elif choice ==4 :
        for i ,item in enumerate(s1.bBooks):
            print(f"{i}. {item}")
        bookName = int(input("Enter Book You Return:"))
        r = s1.bBooks[bookName]
        s1.returnBook(bookName)
        print(f"{r} Book Returned")
    elif choice == 5:
        break
    else:
        print("Enter Valid Choice")

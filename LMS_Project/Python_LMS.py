import datetime,os

print("My current working directory is :", os.getcwd())

class LMS:
    """This class is used to keep record of books library.
    It comprises of four modules: Display books,Issue books,Return books,Add books
    """
    def __init__(self,list_of_books,library_name):
        self.list_of_books="List_of_books.txt"
        self.library_name=library_name
        self.dict_books={}
        Id=101
        with open(self.list_of_books) as bk:
            content=bk.readlines()
            for line in content:
                self.dict_books.update({str(Id):{"books_title":line.replace("\n",""),"lender_name":"","Issue_date":"","Status":"Available"}})
                Id+=1
    def displaybooks(self):
        print("****************List of Books*************************")
        print("Books ID:","Title",sep="\t")
        print("******************************************************")
        for key,value in self.dict_books.items():
            print(key,"\t\t",value.get("books_title"),"-[",value.get("Status"),"]")

    def Issuebooks(self):
        books_id=input("enter book's Id: ")
        current_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if books_id in self.dict_books.keys():
            if not self.dict_books[books_id]['Status']=="Available":
                print(f"This book is already issued to {self.dict_books[books_id]['lender_name']} on {self.dict_books[books_id]['lend_date']}")
                return self.Issuebooks()
            elif self.dict_books[books_id]["Status"]=="Available":
                your_name=input("Enter your name:")
                self.dict_books[books_id]["lender_name"]=your_name
                self.dict_books[books_id]["Issue_date"]=current_date
                self.dict_books[books_id]["Status"] = "Already Issued"
                print(f"Book issued successfully the issue status changed to {self.dict_books[books_id]['Status']}")
        else:
            print("Book ID not found")
            return self.Issuebooks()

    def addbooks(self):
        new_books=input("enter the book title: ")
        if new_books == "":
            return self.addbooks()
        elif len(new_books) > 25:
            print("Books title is too lengthy 20 char atmost is advisible")
            return  self.addbooks()
        else:
            with open(self.list_of_books , "a") as bk:
                bk.writelines(f"{new_books}\n")
                self.dict_books.update({str(int(max(self.dict_books))+1):{"books_title":new_books,"lender_name":"","Issue_date":"","Status":"Available"}})
                print(f"This book {new_books} has been added to the library successfully")
    def returnbooks(self) :
        books_id= input("enter book's Id: ")
        if books_id in self.dict_books.keys():
            if  self.dict_books[books_id]['Status'] == "Available":
                print("This book is already available in the library.Please recheck your book ID")
                return returnbooks()
            elif not self.dict_books[books_id]['Status'] == "Available":
                self.dict_books[books_id]["lender_name"] = ""
                self.dict_books[books_id]["Issue_date"] = ""
                self.dict_books[books_id]['Status'] = "Available"
                print("Successfully Returned!!\n")



try:
    my_LMS=LMS("list_of_books.txt","Python Library") # class object
    press_key_list={"D":"Display Books","I":"Issue Books","A":"Add books","R":"Return Books","Q":"Quit"}
    key_press="None"
    while not (key_press == "q"):
        print(f"\n--------------------Welcome To {my_LMS.library_name} Library Management System -------------------\n")
        for key,value in press_key_list.items():
            print("Press ",key,"To",value)
            key_press=input("Press key:").casefold()
            if key_press == "i":
                print(f"\n Current Selection:{press_key_list.get(key_press.upper())}")
                my_LMS.Issuebooks()
            elif key_press == 'a':
                print(f"\n Current Selection:{press_key_list.get(key_press.upper())}")
                my_LMS.addbooks()
            elif key_press == 'd':
                print(f"\n Current Selection:{press_key_list.get(key_press.upper())}")
                #print(f"\n Current Selection: Display Books")
                my_LMS.displaybooks()
            elif key_press == 'r':
                print(f"\n Current Selection:{press_key_list.get(key_press.upper())}")
                my_LMS.returnbooks()
            elif key_press == 'q':
                break
            else:
                continue
except Exception as e:
    print(" Something went wrong.Please check your input !!!")





#print(l.displaybooks())




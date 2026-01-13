class Ebook:
    def __init__(self,title,author,num_pages,curr_page):
        self.title=title
        self.author=author
        self.pages=num_pages
        self.current_page=curr_page
        self.is_open= False

    def book_open(self):
        self.is_open=True

    def book_close(self):
        self.is_open=False

    def go_forward(self):
        if self.is_open:
            self.current_page+=1

    def go_back(self):
        if self.is_open:
            self.current_page-=1
    
    def display_data(self):
        if self.is_open:
            print(f'Name - {self.title}, author - {self.author}, number of pages - {self.pages}, book is open on the page {self.current_page}')
        else:
            print(f'Name - {self.title}, author - {self.author}, number of pages - {self.pages}, book is closed')

book1= Ebook('Harry Potter','J. K. Rowling',400,5)
book1.book_open()
book1.go_forward()
book1.go_forward()
book1.go_forward()
book1.go_forward()
book1.book_close()
book1.display_data()



         

    

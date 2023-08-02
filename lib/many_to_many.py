from datetime import datetime

class Author:
    all=[]
    def __init__(self, name):
        self.name=name
        self.contracts_list=[]
        Author.all.append(self)
    def contracts(self):
        return self.contracts_list
    def books(self):
        return [contract.book for contract in self.contracts_list]
    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self.contracts_list.append(contract)
        return contract
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts_list)

class Book:
    all=[]
    def __init__(self, title):
        self.title=title
        self.contracts_list=[]
        Book.all.append(self)
    def contracts(self):
        return self.contracts_list 
    def authors(self):
        return [contract.author for contract in self.contracts_list]

class Contract:
    all=[]
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")
        self.author=author
        self.book=book
        self.date=date
        self.royalties= royalties

        author.contracts_list.append(self)
        book.contracts_list.append(self)

        Contract.all.append(self)
    @classmethod
    def contracts_by_date(cls):
        return sorted(cls.all, key=lambda contract: datetime.strptime(contract.date, '%m/%d/%Y'))
        
            

#same_date_contracts = Contract.contracts_by_date("01/01/2023")
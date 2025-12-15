import csv
with open('books.csv','r') as books:
    content=csv.reader(books)
    next(content)
    for line in content:
        if line[2]=='Fantasy':
            with open('books_fantasy.txt','a') as fantasy:
                fantasy.write(f'{line}\n')
        elif line[2]=='Romance':
            with open('books_romance.txt','a') as romance:
                romance.write(f'{line}\n')
        elif line[2]=='Historical':
            with open('books_historical.txt','a') as historical:
                historical.write(f'{line}\n')
        elif line[2]=='Classic':
            with open('books_classic.txt','a') as classic:
                classic.write(f'{line}\n')

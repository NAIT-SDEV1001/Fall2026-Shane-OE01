#import the Path class
from pathlib import Path


#open --> read/write --> close

def read_all_books(file_path):
    try:
        #open a connection to the file for reading
        #file_path - path to your file
        #'r' - open the file for reading(the mode)
        #encoding - how the text is encoded on the file
        #as file - reference called file to that connection

        with open(file_path,'r',encoding='utf-8') as file:
            #readlines returns a list of the lines on the file
            books = file.readlines()
          
        return [book.strip() for book in books]

    except FileNotFoundError:
        return None

def main():
    #what is the path of the current file?
    #path to py file-->get the parent folder -->look there for the txt file
    file_path = Path(__file__).parent/'books.txt'
    books = read_all_books(file_path)

    if books is None:
        print("That book file cannot be found!")
    else:
        print(books)
        #Loop through books list
        for book in books:
            print(book)

if __name__ == '__main__':
    main()





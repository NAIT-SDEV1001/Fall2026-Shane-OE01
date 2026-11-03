from pathlib import Path

def read_book_directly(file_path):
    try: 
        with open(file_path,'r',encoding='utf-8') as file:
            books = [book.strip() for book in file if book.strip()]
            # for book in file:
            #     if book.strip():
            #         books.append(book.strip())
        return books
    except FileNotFoundError:    
        return None

def main():
    file_path = Path(__file__).parent/'books.txt'
    books = read_book_directly(file_path)

    if books is None:
        print("The books list is empty")
    else:
        for book in books:
            print(book)

if __name__ == '__main__':
    main()